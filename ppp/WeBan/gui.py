import tkinter as tk
from tkinter import ttk, messagebox
import sys
import threading
import traceback
from io import StringIO
from typing import Optional

# 导入日志模块
from loguru import logger
from main import run_weban_task


class ThreadSafeTextRedirector:
    """线程安全的文本重定向器"""
    def __init__(self, text_widget, root):
        self.text_widget = text_widget
        self.root = root
        self.buffer = StringIO()
        self.lock = threading.Lock()

    def write(self, text):
        """写入文本（线程安全）"""
        with self.lock:
            self.buffer.write(text)
            self.root.after(0, self._write_to_widget, text)

    def _write_to_widget(self, text):
        """实际写入到文本部件（在主线程中执行）"""
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)

    def flush(self):
        """刷新缓冲区"""
        with self.lock:
            content = self.buffer.getvalue()
            self.buffer = StringIO()
        return content


class WeBanGUI:
    """WeBan客户端图形界面"""
    def __init__(self, root):
        self.root = root
        self.root.title("WeBan学习助手")
        self.task_cancelled = False
        self.task_thread: Optional[threading.Thread] = None
        self.setup_ui()
        self.redirect_output()

    def setup_ui(self):
        """设置用户界面"""
        # 配置窗口网格布局
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # 创建输入框标签和部件
        input_widgets = [
            ("学校：", "school_entry"),
            ("账号：", "username_entry"),
            ("密码：", "password_entry"),
            ("学习时长(秒)：", "study_time_entry")  # 将分钟改为秒
        ]

        for i, (label_text, attr_name) in enumerate(input_widgets):
            tk.Label(self.root, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky="w")
            if label_text == "密码：":
                widget = tk.Entry(self.root, show="*")
            elif label_text == "学习时长(秒)：":  # 匹配更新后的标签
                widget = tk.Entry(self.root)
                widget.insert(0, "15")  # 默认值保持15（现为15秒）
            else:
                widget = tk.Entry(self.root)
            widget.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            setattr(self, attr_name, widget)

        # 创建控制台文本框和滚动条
        console_frame = ttk.Frame(self.root)
        console_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        console_frame.grid_rowconfigure(0, weight=1)
        console_frame.grid_columnconfigure(0, weight=1)

        self.console = tk.Text(console_frame, wrap=tk.WORD)
        self.console.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(console_frame, command=self.console.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.console.config(yscrollcommand=scrollbar.set)

        # 创建按钮框架
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)

        # 提交按钮
        self.submit_btn = tk.Button(button_frame, text="开始学习", command=self.start_task)
        self.submit_btn.pack(side=tk.LEFT, padx=10)

        # 取消按钮
        self.cancel_btn = tk.Button(button_frame, text="取消", command=self.cancel_task, state="disabled")
        self.cancel_btn.pack(side=tk.LEFT, padx=10)

        # 清除日志按钮
        self.clear_btn = tk.Button(button_frame, text="清除日志", command=self.clear_log)
        self.clear_btn.pack(side=tk.LEFT, padx=10)

    def redirect_output(self):
        """重定向标准输出和错误到控制台文本框"""
        self.redirector = ThreadSafeTextRedirector(self.console, self.root)
        sys.stdout = self.redirector
        sys.stderr = self.redirector

        # 配置日志
        logger.remove()
        logger.add(self.redirector.write, level="INFO")
        logger.info("WeBan学习助手已启动")

    def start_task(self):
        """开始学习任务"""
        # 获取输入值
        school = self.school_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        study_time_text = self.study_time_entry.get().strip()

        # 验证输入
        if not all([school, username, password]):
            messagebox.showerror("输入错误", "学校、账号和密码不能为空！")
            return

        try:
            study_time = int(study_time_text) if study_time_text else 15
            if study_time <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("输入错误", "学习时长(秒)必须是正整数！")  # 添加单位说明
            return

        # 更新按钮状态
        self.submit_btn.config(state="disabled")
        self.cancel_btn.config(state="normal")
        self.task_cancelled = False
        logger.info("\n--- 开始执行学习任务 ---\n")

        # 启动任务线程
        self.task_thread = threading.Thread(
            target=self.run_task_thread,
            args=(school, username, password, study_time),
            daemon=True
        )
        self.task_thread.start()

    def run_task_thread(self, school, username, password, study_time):
        """在后台线程中运行任务"""
        try:
            success = run_weban_task(school, username, password, study_time)
            result = "成功" if success else "失败"
            logger.info(f"\n--- 学习任务执行{result} ---\n")
            if not success and not self.task_cancelled:
                self.root.after(0, lambda: messagebox.showerror("任务失败", "学习任务执行失败，请查看日志了解详情"))
        except Exception as e:
            if not self.task_cancelled:
                logger.error(f"任务执行出错: {str(e)}")
                traceback.print_exc()
                self.root.after(0, lambda: messagebox.showerror("执行错误", f"任务执行出错: {str(e)}"))
        finally:
            # 恢复UI状态
            self.root.after(0, self._task_complete)

    def _task_complete(self):
        """任务完成后更新UI"""
        self.submit_btn.config(state="normal")
        self.cancel_btn.config(state="disabled")
        self.task_thread = None

    def cancel_task(self):
        """取消当前任务"""
        if self.task_thread and self.task_thread.is_alive():
            self.task_cancelled = True
            self.cancel_btn.config(state="disabled")
            logger.info("\n--- 正在取消任务... ---\n")

    def clear_log(self):
        """清除日志"""
        self.console.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  # 初始窗口大小
    app = WeBanGUI(root)
    root.mainloop()