import json
import os
import sys
import time
import webbrowser
from random import randint
from typing import Any, Dict, Optional, TYPE_CHECKING, Union
from urllib.parse import parse_qs, urlparse
import base64
import io
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

from loguru import logger
import re

from api import WeBanAPI

if TYPE_CHECKING:
    from ddddocr import DdddOcr

if getattr(sys, "frozen", False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))
answer_dir = os.path.join(base_path, "answer")
answer_path = os.path.join(answer_dir, "answer.json")


def clean_text(text):
    # 只保留字母、数字和汉字，自动去除所有符号和空格
    return re.sub(r"[^\w\u4e00-\u9fa5]", "", text)


class SimpleOcr:
    """
    基于PIL和numpy的自定义OCR实现
    专门针对简单验证码进行优化
    """
    
    def classification(self, img_bytes):
        """
        对验证码图像进行分类识别
        输入：图像字节数据
        输出：识别出的验证码字符串
        """
        try:
            # 保存验证码图像到文件，以便调试和手动输入
            with open('verify_code_debug.png', 'wb') as f:
                f.write(img_bytes)
            
            # 将字节数据转换为PIL图像
            image = Image.open(io.BytesIO(img_bytes))
            
            # 图像预处理
            processed_image = self._preprocess_image(image)
            
            # 保存处理后的图像
            processed_image.save('verify_code_processed.png')
            
            # 字符分割
            characters = self._segment_characters(processed_image)
            
            # 保存分割后的字符用于调试
            if len(characters) > 0:
                # 创建调试图像
                debug_img = Image.new('L', (len(characters) * 20, 25), 255)
                for i, char_img in enumerate(characters):
                    # 确保字符图像是PIL Image对象
                    if isinstance(char_img, np.ndarray):
                        char_img = Image.fromarray(char_img)
                    # 调整大小以便于查看
                    resized_char = char_img.resize((16, 16), Image.Resampling.NEAREST)
                    debug_img.paste(resized_char, (i * 20 + 2, 4))
                debug_img.save('verify_code_debug.png')
                print(f"Debug - 已保存分割后的字符图像到 verify_code_debug.png")
            
            # 字符识别
            result = []
            char_debug_info = []
            for i, char_img in enumerate(characters):
                char = self._recognize_character(char_img)
                if char:
                    result.append(char)
                    char_debug_info.append(f"字符{i+1}: {char}")
            
            # 如果识别结果不足4位，补充随机字符
            while len(result) < 4:
                random_char = self._generate_random_char()
                result.append(random_char)
                char_debug_info.append(f"字符{len(result)}: {random_char} (随机)")
            
            # 限制结果为4位
            recognized_code = ''.join(result[:4])
            print(f"Debug - 识别结果: {recognized_code}, 分割字符数: {len(characters)}")
            if char_debug_info:
                print(f"Debug - 字符详情: {', '.join(char_debug_info)}")
            
            return recognized_code
        except Exception as e:
            print(f"OCR识别错误: {e}")
            # 发生错误时，尝试基于像素统计的简单识别
            try:
                return self._simple_fallback_ocr(img_bytes)
            except:
                # 返回随机4位验证码
                return ''.join([self._generate_random_char() for _ in range(4)])
    
    def _simple_fallback_ocr(self, img_bytes):
        """
        简单的回退OCR方法，仅基于像素统计
        """
        image = Image.open(io.BytesIO(img_bytes)).convert('L')
        img_array = np.array(image)
        
        # 应用简单阈值
        threshold = 128
        img_array = (img_array < threshold).astype(np.uint8) * 255
        
        # 简单的字符区域检测
        h, w = img_array.shape
        # 寻找非空白列
        column_sums = img_array.sum(axis=0)
        non_zero_cols = np.where(column_sums > 0)[0]
        
        if len(non_zero_cols) == 0:
            return 'AAAA'  # 空图像的默认返回
        
        # 等距分割为4个字符
        start, end = non_zero_cols[0], non_zero_cols[-1]
        char_width = max(2, (end - start + 1) // 4)
        
        result = []
        for i in range(4):
            char_start = start + i * char_width
            char_end = min(end + 1, char_start + char_width)
            char_region = img_array[:, char_start:char_end]
            
            # 计算该区域的黑色像素数
            black_pixels = np.sum(char_region == 0)
            total_pixels = char_region.size
            density = black_pixels / total_pixels if total_pixels > 0 else 0
            
            # 基于密度简单分类
            if density < 0.2:
                result.append(random.choice(['1', 'I', 'L']))
            elif density < 0.35:
                result.append(random.choice(['2', '7', 'T', 'Z']))
            elif density < 0.5:
                result.append(random.choice(['A', 'E', 'F', 'H', 'K', 'N', 'P', 'R', 'S', 'X', 'Y']))
            else:
                result.append(random.choice(['0', 'B', 'C', 'D', 'G', 'O', 'Q', '8', '9']))
        
        return ''.join(result)
    
    def _preprocess_image(self, image):
        """
        图像预处理：灰度转换、对比度增强、去噪、二值化
        优化版本：使用动态对比度和自适应阈值
        """
        try:
            # 转换为灰度图像
            if image.mode != 'L':
                image = image.convert('L')
            
            # 动态对比度增强 - 根据图像特征调整对比度
            img_array = np.array(image)
            brightness_std = np.std(img_array)
            contrast_factor = 3.2 if brightness_std > 80 else 3.8  # 更精确的对比度调整
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(contrast_factor)
            
            # 改进的去噪流程：先高斯模糊再中值滤波
            image = image.filter(ImageFilter.GaussianBlur(radius=1))
            try:
                # PIL的MedianFilter只支持奇数尺寸
                image = image.filter(ImageFilter.MedianFilter(size=3))
            except ValueError:
                # 如果3也不行，使用默认尺寸
                image = image.filter(ImageFilter.MedianFilter())
            
            # 锐化图像以增强字符边缘
            image = image.filter(ImageFilter.SHARPEN)
            
            # 自适应阈值二值化
            img_array = np.array(image)
            try:
                # 尝试使用局部自适应阈值
                from scipy.ndimage import gaussian_filter
                img_float = img_array.astype(float)
                # 计算局部均值
                blurred_float = gaussian_filter(img_float, sigma=2.0)
                # 自适应阈值：当前像素与局部均值的差异
                binary = np.where(img_float < blurred_float * 0.85, 0, 255)
                image = Image.fromarray(binary.astype(np.uint8))
            except:
                # 备选方案：使用改进的全局阈值
                threshold = min(135, max(95, np.mean(img_array) * 0.85))
                image = image.point(lambda p: 255 if p > threshold else 0, '1')
            
            # 形态学操作 - 先膨胀再腐蚀，连接断裂的字符并去除噪点
            try:
                img_array = np.array(image)
                # 创建结构元素
                kernel = np.ones((2, 2), np.uint8)
                # 膨胀操作
                dilated = cv2.dilate(img_array, kernel, iterations=1)
                # 腐蚀操作
                eroded = cv2.erode(dilated, kernel, iterations=1)
                image = Image.fromarray(eroded)
            except:
                # 如果OpenCV不可用，跳过此步骤
                pass
            
            # 保存调试图像（可选）
            # image.save('debug_preprocessed.png')
            
            return image
        except Exception as e:
            print(f"预处理错误: {str(e)}")
            # 出错时返回原始灰度图
            return image.convert('L')
    
    def _segment_characters(self, image):
        """
        字符分割：将图像分割为单个字符
        优化版本：使用聚类算法和字符居中技术
        """
        try:
            # 将图像转换为numpy数组
            img_array = np.array(image)
            h, w = img_array.shape
            
            # 找到所有非空白列
            column_sums = img_array.sum(axis=0)
            non_zero_cols = np.where(column_sums < h * 255)[0]  # 寻找有黑色像素的列
            
            if len(non_zero_cols) == 0:
                # 如果没有找到非空白列，返回空列表
                return []
            
            # 字符分割结果
            characters = []
            min_char_width = 3  # 增加最小字符宽度以过滤噪点
            
            # 1. 尝试使用DBSCAN聚类进行字符分割（如果scikit-learn可用）
            try:
                from sklearn.cluster import DBSCAN
                
                # 准备聚类数据
                X = np.array(non_zero_cols).reshape(-1, 1)
                
                # DBSCAN聚类 - 动态调整参数
                cluster_dist = max(3, (non_zero_cols[-1] - non_zero_cols[0]) // 12)
                clustering = DBSCAN(eps=cluster_dist, min_samples=2).fit(X)
                
                # 获取唯一的聚类标签（排除噪声点）
                unique_labels = set(clustering.labels_)
                unique_labels.discard(-1)
                
                # 处理每个聚类作为一个字符
                char_clusters = []
                for label in unique_labels:
                    # 获取该聚类的所有列
                    cluster_cols = [non_zero_cols[i] for i, l in enumerate(clustering.labels_) if l == label]
                    if len(cluster_cols) > 0:
                        start = min(cluster_cols)
                        end = max(cluster_cols)
                        char_clusters.append((start, end))
                
                # 按位置排序
                char_clusters.sort(key=lambda x: x[0])
                
                # 从聚类中提取字符
                for start, end in char_clusters:
                    # 确保字符宽度足够
                    if end - start >= min_char_width:
                        char_array = img_array[:, start:end+1]
                        char_img = Image.fromarray(char_array)
                        # 使用居中调整而不是简单的resize
                        centered_img = self._center_and_resize(char_img)
                        characters.append(centered_img)
                
            except ImportError:
                # 如果scikit-learn不可用，使用传统方法
                pass
            
            # 2. 如果聚类方法没有得到足够的字符，使用自适应分割
            if len(characters) < 4:
                characters = []
                # 计算字符区域
                start_col = non_zero_cols[0]
                end_col = non_zero_cols[-1] + 1
                total_width = end_col - start_col
                
                # 确保有足够的宽度进行分割
                if total_width >= 4 * min_char_width:
                    # 智能等距分割
                    char_width = total_width // 4
                    # 添加微小的调整以适应实际字符位置
                    adjustments = [0, 0, 0, 0]
                    
                    # 分析每列的像素密度
                    for i in range(4):
                        # 预测字符位置
                        pred_center = start_col + i * char_width + char_width // 2
                        # 查找实际的密度峰值位置
                        search_range = max(3, char_width // 2)
                        search_start = max(start_col, pred_center - search_range)
                        search_end = min(end_col, pred_center + search_range)
                        
                        # 计算搜索范围内的像素密度
                        if search_end > search_start:
                            max_density = 0
                            best_pos = pred_center
                            for pos in range(search_start, search_end - 2):
                                window = img_array[:, pos:pos+3]
                                density = np.sum(window == 0) / (h * 3)
                                if density > max_density:
                                    max_density = density
                                    best_pos = pos
                            
                            # 调整字符位置
                            adjustments[i] = best_pos - pred_center
                    
                    # 应用调整并分割字符
                    for i in range(4):
                        char_start = start_col + i * char_width + adjustments[i]
                        char_end = char_start + char_width
                        # 确保边界有效
                        char_start = max(start_col, char_start - 1)
                        char_end = min(end_col, char_end + 1)
                        
                        if char_end - char_start >= min_char_width:
                            char_array = img_array[:, char_start:char_end]
                            char_img = Image.fromarray(char_array)
                            centered_img = self._center_and_resize(char_img)
                            characters.append(centered_img)
            
            # 3. 最后的兜底方案：简单等距分割
            if len(characters) < 4:
                characters = []
                # 计算字符区域
                start_col = non_zero_cols[0]
                end_col = non_zero_cols[-1] + 1
                total_width = end_col - start_col
                
                # 确保有足够的宽度进行分割
                if total_width >= 4 * min_char_width:
                    char_width = total_width // 4
                    for i in range(4):
                        char_start = start_col + i * char_width
                        char_end = char_start + char_width
                        if char_end <= end_col and char_end - char_start >= min_char_width:
                            char_array = img_array[:, char_start:char_end]
                            char_img = Image.fromarray(char_array)
                            centered_img = self._center_and_resize(char_img)
                            characters.append(centered_img)
        
        except Exception as e:
            print(f"字符分割错误: {str(e)}")
            # 出错时返回等距分割的字符
            characters = []
            w = image.width
            h = image.height
            min_char_width = 3
            
            # 计算字符区域
            char_width = w // 4
            for i in range(4):
                char_start = i * char_width
                char_end = char_start + char_width
                if char_end - char_start >= min_char_width:
                    char_img = image.crop((char_start, 0, char_end, h))
                    try:
                        centered_img = self._center_and_resize(char_img)
                        characters.append(centered_img)
                    except:
                        # 如果居中失败，使用简单resize
                        char_img = char_img.resize((16, 16), Image.Resampling.LANCZOS)
                        characters.append(char_img)
        
        # 确保返回4个字符（如果不足，用空白图像补充）
        while len(characters) < 4:
            # 创建空白图像
            blank_img = Image.new('L', (16, 16), 255)
            characters.append(blank_img)
        
        return characters[:4]
    
    def _center_and_resize(self, char_img):
        """
        将字符居中并调整大小，确保字符在图像中央并保持比例
        这对于提高字符识别准确率至关重要
        """
        try:
            # 将图像转换为数组
            array = np.array(char_img)
            h, w = array.shape
            
            # 找到字符的实际边界
            # 寻找有黑色像素的行和列
            rows_with_text = np.where(np.sum(array == 0, axis=1) > 0)[0]
            cols_with_text = np.where(np.sum(array == 0, axis=0) > 0)[0]
            
            if len(rows_with_text) > 0 and len(cols_with_text) > 0:
                # 裁剪到字符边界
                top = rows_with_text[0]
                bottom = rows_with_text[-1]
                left = cols_with_text[0]
                right = cols_with_text[-1]
                
                # 裁剪图像
                cropped = array[top:bottom+1, left:right+1]
                cropped_h, cropped_w = cropped.shape
                
                # 创建一个16x16的空白图像（白色背景）
                centered = np.ones((16, 16), dtype=np.uint8) * 255
                
                # 计算缩放因子，保留适当的边距
                max_dim = max(cropped_h, cropped_w)
                scale = 12 / max_dim  # 保留2像素的边距
                
                # 计算新的尺寸
                new_h = int(cropped_h * scale)
                new_w = int(cropped_w * scale)
                
                # 确保尺寸有效
                new_h = max(1, new_h)
                new_w = max(1, new_w)
                
                # 使用PIL进行高质量缩放
                from PIL import Image
                cropped_img = Image.fromarray(cropped)
                resized = cropped_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                resized_array = np.array(resized)
                
                # 计算居中位置
                y_offset = (16 - new_h) // 2
                x_offset = (16 - new_w) // 2
                
                # 将调整大小后的字符放置在居中位置
                centered[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized_array
                
                return Image.fromarray(centered)
            else:
                # 如果没有找到字符，返回空白图像
                return Image.new('L', (16, 16), 255)
        except Exception:
            # 出错时使用简单的调整大小作为兜底
            return char_img.resize((16, 16), Image.Resampling.LANCZOS)
        
        # 4. 如果所有方法都失败，使用固定分割
        if len(characters) < 4:
            characters = []
            # 简单地将图像等分为4部分
            total_width = w
            char_width = total_width // 4
            for i in range(4):
                char_start = i * char_width
                char_end = char_start + char_width
                char_array = img_array[:, char_start:char_end]
                char_img = Image.fromarray(char_array)
                char_img = char_img.resize((16, 16), Image.Resampling.LANCZOS)
                characters.append(char_img)
        
        # 确保最多返回4个字符
        return characters[:4]
    
    def _recognize_character(self, char_img):
        """
        单个字符识别：基于像素特征进行更精确的模式匹配
        改进的字符识别算法，增加更多特征和更准确的匹配规则
        """
        # 将字符图像转换为numpy数组
        char_array = np.array(char_img)
        h, w = char_array.shape
        
        # 计算基础特征
        # 1. 黑色像素总数
        black_pixels = np.sum(char_array == 0)
        
        # 2. 像素密度
        pixel_density = black_pixels / (h * w)
        
        # 3. 水平和垂直中心线特征
        center_y = h // 2
        center_x = w // 2
        horizontal_center = np.sum(char_array[center_y, :] == 0)
        vertical_center = np.sum(char_array[:, center_x] == 0)
        
        # 4. 边缘像素特征
        top_edge = np.sum(char_array[0, :] == 0)
        bottom_edge = np.sum(char_array[-1, :] == 0)
        left_edge = np.sum(char_array[:, 0] == 0)
        right_edge = np.sum(char_array[:, -1] == 0)
        
        # 5. 区域特征
        top_third = np.sum(char_array[:h//3, :] == 0)
        middle_third = np.sum(char_array[h//3:2*h//3, :] == 0)
        bottom_third = np.sum(char_array[2*h//3:, :] == 0)
        
        # 6. 对称性特征
        left_half = np.sum(char_array[:, :w//2] == 0)
        right_half = np.sum(char_array[:, w//2:] == 0)
        symmetry_ratio = min(left_half, right_half) / max(left_half, right_half + 1)  # 避免除零
        
        # 7. 检查横线和竖线
        def has_horizontal_line(array, threshold=0.6):
            """检查是否有水平横线"""
            rows = []
            for i in range(array.shape[0]):
                row_sum = np.sum(array[i, :] == 0)
                if row_sum >= array.shape[1] * threshold:
                    rows.append(i)
            return rows
        
        def has_vertical_line(array, threshold=0.6):
            """检查是否有垂直竖线"""
            cols = []
            for i in range(array.shape[1]):
                col_sum = np.sum(array[:, i] == 0)
                if col_sum >= array.shape[0] * threshold:
                    cols.append(i)
            return cols
        
        h_lines = has_horizontal_line(char_array)
        v_lines = has_vertical_line(char_array)
        
        # 8. 额外特征：上下左右区域
        left_region = np.sum(char_array[:, :w//4] == 0)
        right_region = np.sum(char_array[:, 3*w//4:] == 0)
        top_region = np.sum(char_array[:h//4, :] == 0)
        bottom_region = np.sum(char_array[3*h//4:, :] == 0)
        
        # 9. 中心区域特征
        center_region = char_array[h//3:2*h//3, w//3:2*w//3]
        center_density = np.sum(center_region == 0) / center_region.size
        
        # 计算额外的区分特征
        # 1. 顶部和底部是否有横线（用于区分I和1）
        has_top_bar = top_edge > w * 0.7
        has_bottom_bar = bottom_edge > w * 0.7
        
        # 2. 左右两侧是否有像素（用于区分不同字符）
        left_side_density = np.sum(char_array[:, :max(1, w//5)] == 0) / (h * max(1, w//5))
        right_side_density = np.sum(char_array[:, -max(1, w//5):] == 0) / (h * max(1, w//5))
        
        # 3. 整体形状特征
        is_tall_thin = w < h * 0.4
        is_square = abs(w - h) < h * 0.2
        
        # 优先识别容易混淆的字符（1, I, L）
        # 计算额外的区分特征
        # 4. 左右边缘的连续性
        left_continuity = self._calculate_edge_continuity(char_array[:, 0])
        right_continuity = self._calculate_edge_continuity(char_array[:, -1])
        
        # 5. 底部横线的宽度比例
        bottom_bar_width_ratio = bottom_edge / w if w > 0 else 0
        
        # 6. 垂直线条比例（衡量竖线的连续性）
        vertical_lines_ratio = 0
        if h > 0 and w > 0:
            # 计算垂直中心线的像素比例
            center_col = w // 2
            vertical_lines_ratio = np.sum(char_array[:, center_col-1:center_col+2] == 0) / (h * 3)
        
        # 添加调试信息，帮助分析特征值
        debug_info = {
            'density': round(pixel_density, 3),
            'shape': 'tall_thin' if is_tall_thin else 'square' if is_square else 'other',
            'h/w': round(h/w, 2) if w > 0 else 0,
            'has_top_bar': has_top_bar,
            'has_bottom_bar': has_bottom_bar,
            'bottom_ratio': round(bottom_bar_width_ratio, 3),
            'left_cont': round(left_continuity, 3),
            'right_cont': round(right_continuity, 3),
            'vert_lines': round(vertical_lines_ratio, 3),
            'left_side': round(left_side_density, 3),
            'right_side': round(right_side_density, 3),
            'h_lines': len(h_lines),
            'v_lines': len(v_lines)
        }
        
        # 为所有字符输出调试信息，便于全面分析
        print(f"Debug - 字符特征: {debug_info}")
        
        # 数字1 - 非常细长，只有一条垂直中线，没有顶部和底部横线
        if is_tall_thin and pixel_density < 0.22:
            # 1的关键特征：极高的垂直线比例，极低的左右区域密度
            if vertical_lines_ratio > 0.8 and not has_top_bar and not has_bottom_bar:
                # 检查中心线以外区域是否几乎没有像素
                center_col = w // 2
                non_center_density = np.sum(char_array[:, :center_col-1] == 0) + np.sum(char_array[:, center_col+2:] == 0)
                non_center_density /= (h * (w - 3)) if w > 3 else 1
                
                debug_info['non_center_density'] = round(non_center_density, 3)
                # 提高阈值，确保只有真正的1才会被识别
                if non_center_density < 0.03 and vertical_center > h * 0.7 and left_side_density < 0.05 and right_side_density < 0.05:
                    print(f"识别为1 - 特征: {debug_info}")
                    return '1'
        
        # 字母I - 细长，必须同时具有顶部和底部横线
        if is_tall_thin and 0.22 < pixel_density < 0.35:
            # I的关键特征：必须同时具有顶部和底部横线
            if has_top_bar and has_bottom_bar:
                # 检查横线的宽度和质量 - 提高阈值确保横线质量
                top_bar_quality = top_edge / w if w > 0 else 0
                bottom_bar_quality = bottom_edge / w if w > 0 else 0
                
                if top_bar_quality > 0.75 and bottom_bar_quality > 0.75:
                    # I的垂直中心线像素分布均匀且连续
                    center_col_density = np.sum(char_array[:, w//2-1:w//2+2] == 0) / (h * 3)
                    
                    # 检查垂直方向的均匀性
                    upper_half_density = np.sum(char_array[:h//2, w//2-1:w//2+2] == 0) / ((h//2) * 3)
                    lower_half_density = np.sum(char_array[h//2:, w//2-1:w//2+2] == 0) / ((h - h//2) * 3)
                    vertical_uniformity = min(upper_half_density, lower_half_density) / max(upper_half_density, lower_half_density + 0.01)
                    
                    debug_info['center_col_density'] = round(center_col_density, 3)
                    debug_info['vertical_uniformity'] = round(vertical_uniformity, 3)
                    
                    # 提高阈值，确保I的识别更准确
                    if center_col_density > 0.7 and vertical_uniformity > 0.8 and vertical_lines_ratio > 0.7:
                        print(f"识别为I - 特征: {debug_info}")
                        return 'I'
        
        # 字母L - 左侧竖线加底部横线，没有顶部横线
        if is_tall_thin and 0.32 < pixel_density < 0.45:
            # L的关键特征：只有底部横线，没有顶部横线，左侧边缘连续性极高
            if not has_top_bar and has_bottom_bar:
                # 检查底部横线的质量和左侧竖线的连续性
                bottom_bar_quality = bottom_edge / w if w > 0 else 0
                
                # 检查左侧区域的密度
                left_region_density = np.sum(char_array[:, :w//3] == 0) / (h * (w//3)) if w > 0 else 0
                right_region_density = np.sum(char_array[:, 2*w//3:] == 0) / (h * (w - 2*w//3)) if w > 0 else 0
                
                debug_info['bottom_bar_quality'] = round(bottom_bar_quality, 3)
                debug_info['left_region_density'] = round(left_region_density, 3)
                debug_info['right_region_density'] = round(right_region_density, 3)
                
                # L的特点：左侧密度高，右侧密度低，底部有横线，且左侧连续性极高
                # 提高阈值，避免过度识别为L
                if bottom_bar_quality > 0.8 and left_region_density > 0.5 and right_region_density < 0.08:
                    # 检查左侧边缘的连续性 - 提高阈值
                    if left_continuity > 0.9 and right_continuity < 0.1:
                        # 额外检查：L的底部横线应该与左侧竖线相连
                        bottom_left_corner = char_array[-1, :5]  # 底部左侧5个像素
                        if np.sum(bottom_left_corner == 0) > 3:  # 确保底部左侧有足够的像素
                            print(f"识别为L - 特征: {debug_info}")
                            return 'L'
        
        # 其他数字识别
        # 数字0 - 环形，接近正方形
        if is_square and 0.38 < pixel_density < 0.52 and symmetry_ratio > 0.8:
            # 检查中心是否为空
            if center_density < 0.4:
                # 检查四个角是否比较空
                corners_empty = char_array[0, 0] == 255 and char_array[0, -1] == 255 and \
                               char_array[-1, 0] == 255 and char_array[-1, -1] == 255
                if corners_empty:
                    return '0'
        
        # 数字2 - 顶部横线，向右下方倾斜
        if 0.28 < pixel_density < 0.42:
            if top_third > bottom_third * 1.3 and right_edge > left_edge * 2.5:
                # 检查顶部是否有横线
                if h_lines and h_lines[0] < h//3:
                    return '2'
        
        # 数字3 - 上下两条横线
        if 0.32 < pixel_density < 0.48:
            if len(h_lines) >= 2 and top_third > 8 and bottom_third > 8:
                # 检查中间部分是否较空
                if middle_third < (top_third + bottom_third) * 0.6:
                    return '3'
        
        # 数字4 - 右侧竖线，顶部横线
        if 0.3 < pixel_density < 0.42:
            if right_edge > h * 0.6 and top_third > bottom_third * 1.5:
                # 检查左侧是否较空
                if left_side_density < 0.2:
                    return '4'
        
        # 数字5 - 顶部横线，右侧竖线，底部横线
        if 0.35 < pixel_density < 0.48:
            if right_edge > 6 and top_third > 8 and bottom_third > 8 and left_edge < 4:
                return '5'
        
        # 数字6 - 环形，底部有横线
        if 0.4 < pixel_density < 0.52:
            if symmetry_ratio > 0.7 and bottom_third > top_third and right_edge > 4:
                # 检查底部是否有横线
                if bottom_edge > w * 0.6:
                    return '6'
        
        # 数字7 - 顶部横线，向右下方斜线
        if 0.28 < pixel_density < 0.38:
            # 7的特点：顶部横线明显，右侧有斜线，没有底部横线
            if top_third > bottom_third * 2.5 and not has_bottom_bar:
                # 确保顶部横线质量
                if top_edge > 5 and top_edge > w * 0.6:
                    # 检查斜线特征：右侧边缘应该有像素，但左侧除顶部外应该较空
                    lower_right_density = np.sum(char_array[h//2:, w//2:] == 0) / (h//2 * w//2) if h > 0 and w > 0 else 0
                    upper_left_density = np.sum(char_array[:h//2, :w//2] == 0) / (h//2 * w//2) if h > 0 and w > 0 else 0
                    
                    debug_info['lower_right_density'] = round(lower_right_density, 3)
                    debug_info['upper_left_density'] = round(upper_left_density, 3)
                    
                    if lower_right_density > 0.3 and upper_left_density < 0.1:
                        print(f"识别为7 - 特征: {debug_info}")
                        return '7'
        
        # 数字8 - 上下两个环形
        if 0.45 < pixel_density < 0.6:
            if symmetry_ratio > 0.8 and top_third > 8 and bottom_third > 8:
                # 检查中间是否有分隔
                middle_density = np.sum(char_array[h//2-2:h//2+2, :] == 0) / (4 * w)
                if middle_density < 0.5:
                    return '8'
        
        # 数字9 - 顶部环形，右侧竖线
        if 0.4 < pixel_density < 0.55:
            if top_third > bottom_third * 1.3 and symmetry_ratio > 0.7:
                # 检查顶部是否有环形特征
                if top_region > 8 and center_density < 0.5:
                    return '9'
        
        # 其他字母识别
        # 字母A - 三角形顶部，中间横线
        if 0.4 < pixel_density < 0.55:
            if len(h_lines) == 1 and h_lines[0] > h//3 and h_lines[0] < 2*h//3:
                if left_edge > 5 and right_edge > 5:
                    # 检查顶部是否较尖
                    top_center = char_array[0, w//2] == 0
                    if not top_center:
                        return 'A'
        
        # 字母B - 左侧竖线，上下两个半环
        if pixel_density > 0.5 and left_edge > h * 0.6:
            if top_third > 8 and middle_third > 8 and bottom_third > 8:
                return 'B'
        
        # 字母C - 左侧开口的曲线
        if 0.3 < pixel_density < 0.45 and symmetry_ratio > 0.7:
            if right_edge < 4 and top_third > 5 and bottom_third > 5:
                return 'C'
        
        # 字母D - 左侧竖线，右侧半环
        if pixel_density > 0.45 and left_edge > h * 0.6:
            if symmetry_ratio > 0.7 and right_edge < h * 0.3:
                return 'D'
        
        # 字母E - 左侧竖线，多条横线
        if pixel_density > 0.4 and left_edge > h * 0.6:
            if len(h_lines) >= 2:
                return 'E'
        
        # 字母F - 左侧竖线，顶部和中部横线
        if 0.35 < pixel_density < 0.45:
            if left_edge > h * 0.6 and len(h_lines) == 2 and bottom_third < 5:
                return 'F'
        
        # 字母G - C形状加底部横线
        if 0.4 < pixel_density < 0.5:
            if right_edge > 5 and bottom_edge > 5 and bottom_third > 8:
                return 'G'
        
        # 字母H - 左右竖线，中间横线
        if 0.4 < pixel_density < 0.5:
            if left_edge > h * 0.6 and right_edge > h * 0.6:
                if len(h_lines) == 1 and h_lines[0] > h//3 and h_lines[0] < 2*h//3:
                    return 'H'
        
        # 字母J - 右侧竖线加底部横线
        if 0.3 < pixel_density < 0.4:
            if right_edge > h * 0.6 and bottom_edge > w * 0.6:
                return 'J'
        
        # 字母K - 左侧竖线，右上和右下斜线
        if 0.35 < pixel_density < 0.45:
            if left_edge > h * 0.6 and len(v_lines) == 0:
                return 'K'
        
        # 字母M - 左右竖线，中间V形
        if pixel_density > 0.5 and left_edge > h * 0.5 and right_edge > h * 0.5:
            if vertical_center < h * 0.4:
                return 'M'
        
        # 字母N - 左右竖线，中间斜线
        if 0.4 < pixel_density < 0.5:
            if left_edge > h * 0.5 and right_edge > h * 0.5:
                # 检查对角线
                diagonal_count = 0
                for i in range(min(h, w)):
                    if char_array[i, i] == 0:
                        diagonal_count += 1
                if diagonal_count > min(h, w) * 0.4:
                    return 'N'
        
        # 字母O - 环形（比0更圆）
        if 0.4 < pixel_density < 0.55 and symmetry_ratio > 0.85:
            # 检查中心是否有空白
            if center_density < 0.3 and is_square:
                # O通常比0更圆
                return 'O'
        
        # 字母P - 左侧竖线，顶部半环
        if 0.4 < pixel_density < 0.5:
            if left_edge > h * 0.6 and bottom_third < top_third * 0.6:
                return 'P'
        
        # 字母Q - O加右下角尾巴
        if 0.4 < pixel_density < 0.55:
            if symmetry_ratio > 0.8 and bottom_third > 8 and right_edge > 5:
                # 检查右下角是否有尾巴
                bottom_right = char_array[3*h//4:, 3*w//4:]
                if np.sum(bottom_right == 0) > 3:
                    return 'Q'
        
        # 字母R - P加右下斜线
        if 0.45 < pixel_density < 0.55:
            if left_edge > h * 0.6 and bottom_third < top_third:
                # 检查右侧是否有斜线特征
                if right_region > 5:
                    return 'R'
        
        # 字母S - 上下弯曲的曲线
        if 0.35 < pixel_density < 0.45:
            if top_third > 5 and middle_third > 5 and bottom_third > 5:
                # 检查是否有弯曲特征
                if not h_lines and not v_lines:
                    return 'S'
        
        # 字母T - 顶部横线，中间竖线
        if 0.3 < pixel_density < 0.4:
            if len(h_lines) == 1 and h_lines[0] < h//4:
                # 确保顶部横线质量和位置
                top_h_line = char_array[h_lines[0], :]
                top_line_quality = np.sum(top_h_line == 0) / w if w > 0 else 0
                
                if top_line_quality > 0.8 and vertical_center > 5 and h_lines[0] < vertical_center + 2:
                    # 检查竖线是否在横线中间
                    center_col = w // 2
                    vertical_line = char_array[h_lines[0]:, center_col-1:center_col+2]
                    vertical_line_quality = np.sum(vertical_line == 0) / vertical_line.size if vertical_line.size > 0 else 0
                    
                    debug_info['top_line_quality'] = round(top_line_quality, 3)
                    debug_info['vertical_line_quality'] = round(vertical_line_quality, 3)
                    
                    if vertical_line_quality > 0.7:
                        print(f"识别为T - 特征: {debug_info}")
                        return 'T'
        
        # 字母U - 左右竖线，底部横线
        if 0.35 < pixel_density < 0.45:
            if left_edge > 5 and right_edge > 5 and bottom_edge > 5:
                if top_third < bottom_third * 0.7:
                    return 'U'
        
        # 字母V - 底部交汇的斜线
        if 0.3 < pixel_density < 0.4:
            # V的特点：底部密度高，顶部密度低，没有横线
            if left_edge < 5 and right_edge < 5 and bottom_third > top_third * 2.0 and not has_top_bar and not has_bottom_bar:
                # 检查V形特征：顶部较窄，底部较宽
                top_half_width = np.sum(char_array[:h//2, :] == 0) / (h//2) if h > 0 else 0
                bottom_half_width = np.sum(char_array[h//2:, :] == 0) / (h - h//2) if h > 0 else 0
                
                debug_info['top_half_width'] = round(top_half_width, 3)
                debug_info['bottom_half_width'] = round(bottom_half_width, 3)
                
                if bottom_half_width > top_half_width * 1.5:
                    print(f"识别为V - 特征: {debug_info}")
                    return 'V'
        
        # 字母W - 底部双V形
        if 0.4 < pixel_density < 0.5:
            if left_edge > 5 and right_edge > 5 and bottom_third > top_third:
                # 检查是否有两个V形特征
                if vertical_center < h * 0.5:
                    return 'W'
        
        # 字母X - 交叉的对角线
        if 0.3 < pixel_density < 0.4:
            # 检查两条对角线
            diag1 = 0
            diag2 = 0
            min_dim = min(h, w)
            for i in range(min_dim):
                if char_array[i, i] == 0:
                    diag1 += 1
                if char_array[i, min_dim-1-i] == 0:
                    diag2 += 1
            if diag1 > min_dim * 0.4 and diag2 > min_dim * 0.4:
                return 'X'
        
        # 字母Y - 顶部分叉，底部竖线
        if 0.3 < pixel_density < 0.4:
            if vertical_center < h * 0.5 and top_third > bottom_third:
                # 检查顶部是否有分叉
                if left_half > 5 and right_half > 5:
                    return 'Y'
        
        # 字母Z - 顶部和底部横线，中间斜线
        if 0.25 < pixel_density < 0.35:
            if len(h_lines) == 2 and h_lines[0] < h//3 and h_lines[1] > 2*h//3:
                # 检查对角线
                diagonal_count = 0
                min_dim = min(h, w)
                for i in range(min_dim):
                    if char_array[i, min_dim-1-i] == 0:
                        diagonal_count += 1
                if diagonal_count > min_dim * 0.4:
                    return 'Z'
        
        # 如果没有匹配到任何字符，返回基于像素密度的最可能字符
        return self._generate_random_char(pixel_density)
    
    def _calculate_edge_continuity(self, edge_column):
        """
        计算边缘列的连续性
        """
        if len(edge_column) == 0:
            return 0
        # 计算连续黑色像素的最大长度
        max_continuous = 0
        current_continuous = 0
        for pixel in edge_column:
            if pixel == 0:  # 黑色像素
                current_continuous += 1
                max_continuous = max(max_continuous, current_continuous)
            else:
                current_continuous = 0
        return max_continuous / len(edge_column)
    
    def _generate_random_char(self, pixel_density=None):
        """
        根据像素密度生成更可能的随机字符
        改进的随机字符生成，避免返回容易混淆的字符
        """
        import random
        
        # 验证码中最常见的字符集（避免容易混淆的字符）
        common_chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        
        # 根据像素密度返回更可能的字符，但避免在低像素密度下只返回1/I/L
        if pixel_density is not None:
            # 更精细的密度区间划分
            if pixel_density < 0.25:
                # 极低密度字符 - 添加更多非混淆字符选择
                # 减少1/I/L的比例，增加其他低密度字符
                choices = ['1', 'I', 'L', '7', 'T', 'V']  # 添加其他低密度字符
                weights = [0.2, 0.2, 0.2, 0.15, 0.15, 0.1]  # 降低1/I/L的权重
                return random.choices(choices, weights=weights, k=1)[0]
            elif pixel_density < 0.3:
                # 低密度字符
                return random.choice(['7', 'T', 'Z', 'V'])
            elif pixel_density < 0.35:
                # 中低密度字符
                return random.choice(['2', '5', 'F', 'J', 'X', 'Y'])
            elif pixel_density < 0.4:
                # 中密度字符
                return random.choice(['3', 'K', 'N', 'S', 'U'])
            elif pixel_density < 0.45:
                # 中高密度字符
                return random.choice(['4', '6', 'A', 'E', 'H', 'P', 'R', 'W'])
            else:
                # 高密度字符
                return random.choice(['0', '8', '9', 'B', 'C', 'D', 'G', 'M', 'O', 'Q'])
        
        return random.choice(common_chars)


def base64_to_image(base64_str):
    """
    将base64编码的字符串转换为PIL图像
    """
    image_data = base64.b64decode(base64_str)
    return Image.open(io.BytesIO(image_data))


def image_to_base64(image):
    """
    将PIL图像转换为base64编码的字符串
    """
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    return base64.b64encode(buffer.getvalue()).decode('utf-8')


class WeBanClient:

    def __init__(self, tenant_name: str, account: str | None = None, password: str | None = None, user: Dict[str, str] | None = None, log=logger) -> None:
        self.log = log
        self.tenant_name = tenant_name.strip()
        self.study_time = 15
        self.ocr = self.get_ocr_instance()
        if user and all([user.get("userId"), user.get("token")]):
            self.api = WeBanAPI(user=user)
        elif all([self.tenant_name, account, password]):
            self.api = WeBanAPI(account=account, password=password)
        else:
            self.api = WeBanAPI()
        self.tenant_code = self.get_tenant_code()
        if self.tenant_code:
            self.api.set_tenant_code(self.tenant_code)
        else:
            raise ValueError("学校代码获取失败，请检查学校全称是否正确")

    @staticmethod
    def get_project_type(project_category: int) -> str:
        """
        获取项目类型
        :param project_category: 项目类型 1.新生安全教育 2.安全课程 3.专题学习 4.军事理论 9.实验室
        :return: 项目类型字符串
        """
        if project_category == 3:
            return "special"
        elif project_category == 9:
            return "lab"
        else:
            return ""

    @staticmethod
    def get_ocr_instance(_cache: Dict[str, Any] = {"ocr": None}) -> Optional[Any]:
        """
        获取OCR实例，优先使用ddddocr，失败则使用自定义的SimpleOcr类
        """
        if not _cache.get("ocr"):
            try:
                # 尝试导入ddddocr
                import ddddocr
                try:
                    _cache["ocr"] = ddddocr.DdddOcr(show_ad=False)
                except TypeError:
                    _cache["ocr"] = ddddocr.DdddOcr()
                print("使用ddddocr进行自动验证码识别")
            except ImportError as e:
                print(f"ddddocr导入失败: {e}，将使用自定义OCR方案")
                # 使用自定义的SimpleOcr类
                _cache["ocr"] = SimpleOcr()
        
        return _cache["ocr"]

    def get_tenant_code(self) -> str:
        """
        获取学校代码
        :return: code
        """
        if not self.tenant_name:
            self.log.error(f"学校全称不能为空")
            return ""
        tenant_list = self.api.get_tenant_list_with_letter()
        if tenant_list.get("code", -1) == "0":
            self.log.info(f"获取学校列表成功")
        tenant_names = []
        maybe_names = []
        for item in tenant_list.get("data", []):
            for entry in item.get("list", []):
                name = entry.get("name", "")
                tenant_names.append(name)
                if self.tenant_name == name.strip():
                    self.log.success(f"找到学校代码: {entry['code']}")
                    return entry["code"]
                if self.tenant_name in name:
                    maybe_names.append(name)
        self.log.error(f"{tenant_names}")
        self.log.error(f"没找到你的学校代码，请检查学校全称是否正确（上面是有效的学校名称）: {self.tenant_name}")
        if maybe_names:
            self.log.error(f"可能的学校名称: {maybe_names}")
        return ""

    def get_progress(self, user_project_id: str, project_prefix: str | None, output: bool = True) -> Dict[str, Any]:
        """
        获取学习进度
        :param output: 是否输出进度信息
        :param user_project_id: 用户项目 ID
        :param project_prefix: 项目前缀
        :return:
        """
        progress = self.api.show_progress(user_project_id)
        if progress.get("code", -1) == "0":
            progress = progress.get("data", {})
            # 推送课
            push_num = progress["pushNum"]
            push_finished_num = progress["pushFinishedNum"]
            # 自选课
            optional_num = progress["optionalNum"]
            optional_finished_num = progress["optionalFinishedNum"]
            # 必修课
            required_num = progress["requiredNum"]
            required_finished_num = progress["requiredFinishedNum"]
            # 考试
            exam_num = progress["examNum"]
            exam_finished_num = progress["examFinishedNum"]
            eta = max(0, self.study_time * (required_num - required_finished_num + optional_num - optional_finished_num + push_num - push_finished_num))
            if output:
                self.log.info(f"{project_prefix} 进度：必修课：{required_finished_num}/{required_num}，推送课：{push_finished_num}/{push_num}，自选课：{optional_finished_num}/{optional_num}，考试：{exam_finished_num}/{exam_num}，预计剩余时间：{eta} 秒")
        return progress

    def login(self) -> Dict | None:
        if self.api.user.get("userId"):
            return self.api.user
        retry_limit = 3
        for i in range(retry_limit + 2):
            if i > 0:
                self.log.warning(f"登录失败，正在重试 {i}/{retry_limit+2} 次")
            verify_time = self.api.get_timestamp(13, 0)
            verify_image = self.api.rand_letter_image(verify_time)
            if i < retry_limit and self.ocr:
                try:
                    verify_code = self.ocr.classification(verify_image)
                    self.log.info(f"自动验证码识别结果: {verify_code}")
                    if len(verify_code) != 4:
                        self.log.warning(f"验证码识别失败，正在重试")
                        continue
                except Exception as e:
                    self.log.error(f"验证码识别异常: {e}")
                    continue
            else:
                open("verify_code.png", "wb").write(verify_image)
                webbrowser.open(f"file://{os.path.abspath('verify_code.png')}")
                verify_code = input(f"请查看 verify_code.png 输入验证码：")
            res = self.api.login(verify_code, int(verify_time))
            if res.get("detailCode") == "67":
                self.log.warning(f"验证码识别失败，正在重试")
                continue
            if self.api.user.get("userId"):
                return self.api.user
            self.log.error(f"登录出错，请检查 config.json 内账号密码，或删除文件后重试: {res}")
            break
        return None

    def run_study(self, study_time: int = 15, restudy_time: int = 0) -> None:
        if study_time:
            self.study_time = study_time

        if restudy_time:
            self.study_time = restudy_time
            self.log.info(f"重新学习模式已开启，所有课程将重新学习，每门课程学习 {self.study_time} 秒")

        my_project = self.api.list_my_project()
        if my_project.get("code", -1) != "0":
            self.log.error(f"获取任务列表失败：{my_project}")
            return

        my_project = my_project.get("data", [])
        if not my_project:
            self.log.error(f"获取任务列表失败")

        completion = self.api.list_completion()
        if completion.get("code", -1) != "0":
            self.log.error(f"获取模块完成情况失败：{completion}")

        showable_modules = [d["module"] for d in completion.get("data", []) if d["showable"] == 1]
        if "labProject" in showable_modules:
            self.log.info(f"加载实验室课程")
            lab_project = self.api.lab_index()
            if lab_project.get("code", -1) != "0":
                self.log.error(f"获取实验室课程失败：{lab_project}")
            my_project.append(lab_project.get("data", {}).get("current", {}))

        for task in my_project:
            project_prefix = task["projectName"]
            self.log.info(f"开始处理任务：{project_prefix}")
            need_capt = []

            # 获取学习进度
            self.get_progress(task["userProjectId"], project_prefix)

            # 聚合类别 1：推送课，2：自选课，3：必修课
            for choose_type in [(3, "必修课", "requiredNum", "requiredFinishedNum"), (1, "推送课", "pushNum", "pushFinishedNum"), (2, "自选课", "optionalNum", "optionalFinishedNum")]:
                categories = self.api.list_category(task["userProjectId"], choose_type[0])
                if categories.get("code") != "0":
                    self.log.error(f"获取 {choose_type[1]} 分类失败：{categories}")
                    continue
                for category in categories.get("data", []):
                    category_prefix = f"{choose_type[1]} {project_prefix}/{category['categoryName']}"
                    self.log.info(f"开始处理 {category_prefix}")
                    if not restudy_time and category["finishedNum"] >= category["totalNum"]:
                        self.log.success(f"{category_prefix} 已完成")
                        continue

                    # 获取学习进度
                    progress = self.get_progress(task["userProjectId"], project_prefix, False)
                    if not restudy_time and progress[choose_type[3]] >= progress[choose_type[2]]:
                        self.log.info(f"{category_prefix} 已达到要求，跳过")
                        break

                    courses = self.api.list_course(task["userProjectId"], category["categoryCode"], choose_type[0])
                    for course in courses.get("data", []):
                        course_prefix = f"{category_prefix}/{course['resourceName']}"
                        # 获取学习进度
                        progress = self.get_progress(task["userProjectId"], category_prefix)
                        if not restudy_time and progress[choose_type[3]] >= progress[choose_type[2]]:
                            self.log.info(f"{category_prefix} 已达到要求，跳过")
                            break

                        self.log.info(f"开始处理课程：{course_prefix}")
                        if not restudy_time and course["finished"] == 1:
                            self.log.success(f"{course_prefix} 已完成")
                            continue

                        self.api.study(course["resourceId"], task["userProjectId"])

                        if "userCourseId" not in course:
                            self.log.success(f"{course_prefix} 完成")
                            continue

                        course_url = self.api.get_course_url(course["resourceId"], task["userProjectId"])["data"] + "&weiban=weiban"
                        query = parse_qs(urlparse(course_url).query)
                        if query.get("csCapt", [None])[0] == "true":
                            self.log.warning(f"课程需要验证码，暂时无法处理...")
                            need_capt.append(course_prefix)
                            continue

                        sleep = 0
                        while sleep < self.study_time:
                            if sleep % 60 == 0:
                                self.log.info(f"{course_prefix} 等待 {self.study_time - sleep} 秒，模拟学习中...")
                            time.sleep(1)
                            sleep += 1

                        if query.get("lyra", [None])[0] == "lyra":  # 安全实训
                            res = self.api.finish_lyra(query.get("userActivityId", [None])[0])
                        elif query.get("weiban", [None])[0] != "weiban":
                            res = self.api.finish_by_token(course["userCourseId"], course_type="open")
                        elif query.get("source", [None])[0] == "moon":
                            res = self.api.finish_by_token(course["userCourseId"], course_type="moon")
                        else:
                            # 检查是否需要验证码
                            token = None
                            if query.get("csCapt", [None])[0] == "true":
                                self.log.warning(f"课程需要验证码，暂时无法处理...")
                                need_capt.append(course_prefix)
                                continue
                                res = self.api.invoke_captcha(course["userCourseId"], task["userProjectId"])
                                if res.get("code", -1) != "0":
                                    self.log.error(f"获取验证码失败：{res}")
                                token = res.get("data", {}).get("methodToken", None)

                            res = self.api.finish_by_token(course["userCourseId"], token)
                            if "ok" not in res:
                                self.log.error(f"{course_prefix} 完成失败：{res}")

                        self.log.success(f"{course_prefix} 完成")

            if need_capt:
                self.log.warning(f"以下课程需要验证码，请手动完成：")
                for c in need_capt:
                    self.log.warning(f" - {c}")

            self.log.success(f"{project_prefix} 课程学习完成")

    def run_exam(self, use_time: int = 250):
        # 加载题库
        answers_json = {}

        with open(answer_path, encoding="utf-8") as f:
            for title, options in json.load(f).items():
                title = clean_text(title)
                if title not in answers_json:
                    answers_json[title] = []
                answers_json[title].extend([clean_text(a["content"]) for a in options.get("optionList", []) if a["isCorrect"] == 1])

        # 获取项目
        projects = self.api.list_my_project()
        if projects.get("code", -1) != "0":
            self.log.error(f"获取考试列表失败：{projects}")
            return

        projects = projects.get("data", [])

        completion = self.api.list_completion()
        if completion.get("code", -1) != "0":
            self.log.error(f"获取模块完成情况失败：{completion}")

        showable_modules = [d["module"] for d in completion.get("data", []) if d["showable"] == 1]
        if "labProject" in showable_modules:
            self.log.info(f"加载实验室课程")
            lab_project = self.api.lab_index()
            if lab_project.get("code", -1) != "0":
                self.log.error(f"获取实验室课程失败：{lab_project}")
            projects.append(lab_project.get("data", {}).get("current", {}))

        for project in projects:
            self.log.info(f"开始考试项目 {project['projectName']}")
            user_project_id = project["userProjectId"]
            # 获取考试计划
            exam_plans = self.api.exam_list_plan(user_project_id)
            if exam_plans.get("code", -1) != "0":
                self.log.error(f"获取考试计划失败：{exam_plans}")
                return
            exam_plans = exam_plans["data"]
            for plan in exam_plans:
                if plan["examFinishNum"] != 0:
                    self.log.success(f"考试项目 {project['projectName']}/{plan['examPlanName']} 最高成绩 {plan['examScore']} 分。已考试次数 {plan['examFinishNum']} 次，还剩 {plan['examOddNum']} 次。需要重考吗(y/N)？")
                    if input().strip().lower() != "y":
                        self.log.info(f"不重考项目 {project['projectName']}")
                        continue
                user_exam_plan_id = plan["id"]
                exam_plan_id = plan["examPlanId"]
                # 是否存在完成的考试记录
                before_paper = self.api.exam_before_paper(plan["id"])
                if before_paper.get("code", -1) != "0":
                    self.log.error(f"考试项目 {project['projectName']}/{plan['examPlanName']} 获取考试记录失败：{before_paper}")
                # before_paper = before_paper.get("data", {})
                # if before_paper.get("isExistedNotSubmit"):
                #     self.log.warning(f"考试项目 {project['projectName']}/{plan['examPlanName']} 存在未提交的考试数据，继续将清除未提交数据（Y/n）:")
                #     if input().lower() == "n":
                #         self.log.error(f"用户取消")
                #         return

                # 预请求
                prepare_paper = self.api.exam_prepare_paper(user_exam_plan_id)
                if prepare_paper.get("code", -1) != "0":
                    self.log.error(f"获取考试信息失败：{prepare_paper}")
                    continue
                prepare_paper = prepare_paper["data"]
                question_num = prepare_paper["questionNum"]
                self.log.info(f"考试信息：用户：{prepare_paper['realName']}，ID：{prepare_paper['userIDLabel']}，题目数：{question_num}，试卷总分：{prepare_paper['paperScore']}，限时 {prepare_paper['answerTime']} 分钟")
                per_time = use_time // prepare_paper["questionNum"]

                # 获取考试题目
                exam_paper = self.api.exam_start_paper(user_exam_plan_id)
                if exam_paper.get("code", -1) != "0":
                    self.log.error(f"获取考试题目失败：{exam_paper}")
                    if exam_paper.get("detailCode") == "10018":
                        self.log.warning(f"考试项目 {project['projectName']}/{plan['examPlanName']} 需要手动处理，请在网站上开启一次考试后重试")
                    continue
                exam_paper = exam_paper.get("data", {})
                question_list = exam_paper.get("questionList", [])
                have_answer = []  # 有答案的题目
                no_answer = []  # 无答案的题目

                for question in question_list:
                    if clean_text(question["title"]) in answers_json:
                        have_answer.append(question)
                    else:
                        no_answer.append(question)

                self.log.info(f"题目总数：{question_num}，有答案的题目数：{len(have_answer)}，无答案的题目数：{len(no_answer)}")
                # correct_rate = len(have_answer) / question_num
                # if correct_rate < 0.9:
                #     self.log.warning(f"题库正确率 {correct_rate} 少于 90%，是否继续考试？（Y/n）")
                #     if input().lower() == "n":
                #         self.log.error(f"用户取消")
                #         continue

                for i, question in enumerate(no_answer):
                    self.log.info(f"[{i}/{len(no_answer)}]题目不在题库中或选项不同，请手动选择答案")
                    print(f"题目类型：{question['typeLabel']}，题目标题：{question['title']}")
                    for j, opt in enumerate(question["optionList"]):
                        print(f"{j + 1}. {opt['content']}")

                    opt_count = len(question["optionList"])
                    start_time = time.time()
                    answers_ids = []

                    while not answers_ids:
                        answer = input("请输入答案序号（多个选项用英文逗号分隔，如 1,2,3,4）：").replace(" ", "").replace("，", ",")
                        candidates = [ans.strip() for ans in answer.split(",") if ans.strip()]
                        if all(ans.isdigit() and 1 <= int(ans) <= opt_count for ans in candidates):
                            answers_ids = [question["optionList"][int(ans) - 1]["id"] for ans in candidates]
                            for ans in candidates:
                                self.log.info(f"选择答案：{ans}，内容：{question['optionList'][int(ans)-1]['content']}")
                        else:
                            self.log.error("输入无效，请重新输入（序号需为数字且在选项范围内）")

                    self.log.info(f"正在提交当前答案")
                    end_time = time.time()
                    if not self.record_answer(user_exam_plan_id, question["id"], round(end_time - start_time), answers_ids, exam_plan_id):
                        raise RuntimeError(f"答题失败，请重新考试：{question}")

                self.log.info(f"手动答题结束，开始答题库中的题目，共 {len(have_answer)} 道题目")
                for i, question in enumerate(have_answer):
                    self.log.info(f"[{i}/{len(have_answer)}]题目在题库中，开始答题")
                    self.log.info(f"题目类型：{question['typeLabel']}，题目标题：{question['title']}")
                    answers = answers_json[clean_text(question["title"])]
                    answers_ids = [option["id"] for option in question["optionList"] if clean_text(option["content"]) in answers]
                    self.log.info(f"等待 {per_time} 秒，模拟答题中...")
                    time.sleep(per_time)
                    if not self.record_answer(user_exam_plan_id, question["id"], per_time + 1, answers_ids, exam_plan_id):
                        raise RuntimeError(f"答题失败，请重新考试：{question}")
                self.log.info(f"完成考试，正在提交试卷...")
                submit_res = self.api.exam_submit_paper(user_exam_plan_id)
                if submit_res.get("code", -1) != "0":
                    raise RuntimeError(f"提交试卷失败，请重新考试：{submit_res}")
                self.log.success(f"试卷提交成功，考试完成，成绩：{submit_res['data']['score']} 分")

    def record_answer(self, user_exam_plan_id: str, question_id: str, per_time: int, answers_ids: list, exam_plan_id: str) -> bool:
        """
        记录答题
        :param user_exam_plan_id: 用户考试计划 ID
        :param question_id: 题目 ID
        :param per_time: 用时
        :param answers_ids: 答案 ID 列表
        :param exam_plan_id: 考试计划 ID
        :return:
        """
        res = self.api.exam_record_question(user_exam_plan_id, question_id, per_time, answers_ids, exam_plan_id)
        if res.get("code", -1) != "0":
            self.log.error(f"答题失败，请重新开启考试：{res}")
            return False
        self.log.info(f"保存答案成功")
        return True

    def sync_answers(self) -> None:
        """
        同步答案
        :return:
        """
        os.makedirs(answer_dir, exist_ok=True)
        if not os.path.exists(answer_path):
            self.log.info(f"题库不存在，正在下载...")
            with open(answer_path, "w", encoding="utf-8") as f:
                f.write(self.api.download_answer())
        try:
            with open(answer_path, encoding="utf-8") as f:
                answers_json = json.load(f)
        except Exception as e:
            self.log.error(f"读取题库失败，请重新下载题库：{e}")
            return

        user_project_ids = [p["userProjectId"] for p in self.api.list_my_project().get("data", [])]
        completion = self.api.list_completion()
        if completion.get("code", -1) != "0":
            self.log.error(f"获取模块完成情况失败：{completion}")

        showable_modules = [d["module"] for d in completion.get("data", []) if d["showable"] == 1]
        if "labProject" in showable_modules:
            self.log.info(f"加载实验室课程")
            lab_project = self.api.lab_index()
            if lab_project.get("code", -1) != "0":
                self.log.error(f"获取实验室课程失败：{lab_project}")
            user_project_ids.append(lab_project.get("data", {}).get("current", {}).get("userProjectId"))
        for user_project_id in user_project_ids:
            for plan in self.api.exam_list_plan(user_project_id).get("data", []):
                for history in self.api.exam_list_history(plan["examPlanId"], plan["examType"]).get("data", []):
                    questions = self.api.exam_review_paper(history["id"], history["isRetake"])["data"].get("questions", [])
                    for answer in questions:
                        title = answer["title"]
                        old_opts = {o["content"]: o["isCorrect"] for o in answers_json.get(title, {}).get("optionList", [])}
                        new_opts = old_opts | {o["content"]: o["isCorrect"] for o in answer.get("optionList", [])}
                        for content in new_opts.keys() - old_opts.keys():
                            self.log.info(f"发现题目：{title} 新选项：{content}")
                        answers_json[title] = {
                            "type": answer["type"],
                            "optionList": [{"content": content, "isCorrect": is_correct} for content, is_correct in new_opts.items()],
                        }

        with open(answer_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(answers_json, indent=2, ensure_ascii=False, sort_keys=True))
            f.write("\n")
