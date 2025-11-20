import json
import os
import time
import webbrowser
from random import randint
from typing import Any, Dict, Optional, TYPE_CHECKING, Union
from urllib.parse import parse_qs, urlparse

from loguru import logger

from api import WeBanAPI

if TYPE_CHECKING:
    from ddddocr import DdddOcr


class WeBanClient:
    """WeBan客户端核心类，处理登录、学习和考试等核心功能"""
    def __init__(self, account: str, password: str, school: str, study_time: int = 15) -> None:
        """
        初始化WeBan客户端
        :param account: 账号
        :param password: 密码
        :param school: 学校名称
        :param study_time: 学习时长(秒)  # 单位从分钟改为秒
        """
        self.account = account
        self.school = school
        self.tenant_code = None
        self.ocr = self._get_ocr_instance()  # 初始化OCR实例
        self.api = WeBanAPI(account, password)
        self.study_time = study_time
        self.fail = []
        self._initialize_tenant()

    def _initialize_tenant(self) -> None:
        """初始化租户信息，获取并设置租户代码"""
        self.tenant_code = self.get_tenant_code()
        if not self.tenant_code:
            raise ConfigurationError(f"无法获取学校 '{self.school}' 的租户代码，请检查配置")
        # 这里可以添加获取租户代码的逻辑
        logger.debug(f"初始化租户信息: {self.school}")

    @staticmethod
    def get_project_type(project_category: int) -> str:
        """
        获取项目类型
        :param project_category: 项目类型 1.新生安全教育 2.安全课程 3.专题学习 4.军事理论 9.实验室
        :return: 项目类型字符串
        """
        project_types = {
            3: "special",
            9: "lab"
        }
        return project_types.get(project_category, "")

    @staticmethod
    def _get_ocr_instance(_cache: Dict[str, Any] = {"ocr": None}) -> Optional[Union["DdddOcr", None]]:
        """
        检查是否安装 ddddocr 库，多次调用返回同一个 DdddOcr 实例
        :param _cache: 缓存OCR实例
        :return: OCR实例或None
        """
        if not _cache["ocr"]:
            try:
                import ddddocr
                _cache["ocr"] = ddddocr.DdddOcr()
                logger.info("成功加载ddddocr验证码识别库")
            except ImportError:
                logger.warning("ddddocr库未安装，验证码识别功能将不可用，请运行 'pip install ddddocr' 进行安装以启用自动识别。")

        return _cache["ocr"]

    def get_verify_code(self) -> tuple[str, str]:
        """获取验证码和时间戳"""
        verify_time = self.api.get_timestamp(frac_len=0)
        captcha_image = self.api.rand_letter_image(verify_time)
        return verify_time, captcha_image

    def login(self, verify_code: str, verify_time: str) -> tuple[bool, str]:
        """
        用户登录（带重试机制）
        :param verify_code: 验证码
        :param verify_time: 时间戳
        :return: (是否成功, 错误信息)
        """
        retry_limit = 3
        for attempt in range(retry_limit + 1):
            try:
                if not self.tenant_code:
                    raise ConfigurationError("租户代码未初始化")

                login_result = self.api.login(verify_code, verify_time)
                if login_result.get("code") == "0" and login_result.get("data", {}).get("token"):
                    logger.info(f"[{self.account}] 登录成功")
                    return True, ""
                
                error_msg = login_result.get("detailCode", "未知错误")
                if attempt < retry_limit:
                    logger.warning(f"登录失败(尝试 {attempt+1}/{retry_limit+1}): {error_msg}，将重试...")
                    time.sleep(2)  # 重试前等待2秒
                    continue
                
                return False, error_msg
                
            except AuthenticationError as e:
                return False, f"认证失败: {e.message}"
            except Exception as e:
                if attempt < retry_limit:
                    logger.warning(f"登录异常(尝试 {attempt+1}/{retry_limit+1}): {str(e)}，将重试...")
                    time.sleep(2)
                    continue
                return False, f"登录失败: {str(e)}"

    def run_study(self) -> bool:
        """执行学习任务"""
        try:
            logger.info(f"[{self.account}] 开始学习，时长: {self.study_time}秒")  # 更新单位显示
            # 这里添加实际学习逻辑
            # client.run_study(study_time)
            time.sleep(self.study_time)  # 移除*60转换，直接使用秒
            logger.info(f"[{self.account}] 学习完成")
            return True
        except Exception as e:
            logger.error(f"学习过程出错: {str(e)}")
            return False

    def sync_answers(self) -> bool:
        """同步答案"""
        try:
            logger.info(f"[{self.account}] 同步答案")
            # 这里添加实际同步答案逻辑
            return True
        except Exception as e:
            logger.error(f"同步答案出错: {str(e)}")
            return False

    def run_task(self) -> bool:
        """执行完整任务流程"""
        try:
            # 获取验证码
            verify_time, captcha_image = self.get_verify_code()
            verify_code = self.ocr.classification(captcha_image) if self.ocr else None

            # 如果没有OCR，需要手动输入验证码
            if not verify_code:
                return False, "需要验证码但无法自动识别"

            # 登录
            login_success, error_msg = self.login(verify_code, verify_time)
            if not login_success:
                return False, f"登录失败: {error_msg}"

            # 执行学习
            if not self.run_study():
                return False, "学习任务失败"

            # 同步答案
            if not self.sync_answers():
                return False, "同步答案失败"

            return True, "任务完成"
        except Exception as e:
            return False, f"任务执行异常: {str(e)}"

    def get_tenant_code(self) -> str | None:
        """
        获取学校代码
        :return: 学校对应的租户代码
        """
        if not self.school:
            logger.error("学校名称(school)未设置")
            return None

        try:
            # 获取学校列表
            tenant_list = self.api.get_tenant_list_with_letter()
            if tenant_list.get("code") != "0":
                logger.error(f"获取学校列表失败: {tenant_list.get('detailCode')}")
                return None

            # 遍历学校列表查找匹配项
            tenant_names = []
            for letter_group in tenant_list.get("data", []):
                for tenant in letter_group.get("list", []):
                    tenant_name = tenant.get("name", "")
                    tenant_names.append(tenant_name)
                    
                    # 支持模糊匹配学校名称
                    if self.school in tenant_name or tenant_name in self.school:
                        self.tenant_code = tenant["code"]
                        self.api.set_tenant_code(self.tenant_code)
                        logger.success(f"找到学校代码: {self.tenant_code} ({tenant_name})")
                        return self.tenant_code

            # 未找到匹配学校时提示可能的选项
            logger.error(f"未找到学校 '{self.school}' 的租户代码\n可用学校列表: {tenant_names[:10]}...")
            return None

        except Exception as e:
            logger.error(f"获取租户代码失败: {str(e)}")
            return None
        