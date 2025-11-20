import json
import time
import logging
from base64 import urlsafe_b64decode, urlsafe_b64encode
from random import choice, randint
from typing import Dict, Optional, Any, Tuple, List, Union
from dataclasses import dataclass

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from requests.adapters import HTTPAdapter, Retry

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 常量定义
DEFAULT_BASEURL = "https://weiban.mycourse.cn"
ENCRYPTION_KEY = urlsafe_b64decode("d2JzNTEyAAAAAAAAAAAAAA==")  # wbs512
DEFAULT_TIMEOUT = (9.05, 15)
RETRY_STATUS_CODES = [429, 500, 502, 503, 504]
RETRY_ALLOWED_METHODS = ["GET", "POST"]
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"


class APIError(Exception):
    """API调用异常基类"""
    def __init__(self, message: str, code: Optional[str] = None, response: Optional[requests.Response] = None):
        self.message = message
        self.code = code
        self.response = response
        super().__init__(f"{message} (错误代码: {code})")


class AuthenticationError(APIError):
    """认证相关异常"""
    pass


class ConfigurationError(APIError):
    """配置相关异常"""
    pass


@dataclass
class APIResponse:
    """API响应数据封装"""
    code: str
    data: Any
    detail_code: str
    success: bool

    @classmethod
    def from_json(cls, json_data: Dict[str, Any]) -> 'APIResponse':
        return cls(
            code=json_data.get("code", "-1"),
            data=json_data.get("data"),
            detail_code=json_data.get("detailCode", "-1"),
            success=json_data.get("code") == "0"
        )


class SessionManager:
    """会话管理器，处理HTTP会话创建和重试逻辑"""
    @staticmethod
    def create_retry_session(baseurl: str, retries: int = 5, backoff_factor: float = 1) -> requests.Session:
        """
        创建带重试机制的会话
        :param baseurl: 基础URL
        :param retries: 最大重试次数
        :param backoff_factor: 退避因子
        :return: 配置好的requests会话
        """
        retry_strategy = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=RETRY_STATUS_CODES,
            allowed_methods=RETRY_ALLOWED_METHODS
        )
        session = requests.Session()
        session.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        session.headers = {
            "User-Agent": USER_AGENT,
            "Referer": f"{baseurl}/",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Dnt": "1",
            "Sec-Gpc": "1",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        }
        return session


class CryptoUtils:
    """加密工具类"""
    @staticmethod
    def encrypt(data: Dict[str, Any]) -> str:
        """
        AES加密
        :param data: 要加密的字典数据
        :return: base64编码的加密字符串
        """
        try:
            json_str = json.dumps(data, separators=(",", ":"))
            cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
            encrypted_data = cipher.encrypt(pad(json_str.encode(), AES.block_size))
            return urlsafe_b64encode(encrypted_data).decode()
        except Exception as e:
            logger.error(f"加密失败: {str(e)}")
            raise APIError(f"数据加密失败: {str(e)}")


class WeBanAPI:
    """WeBan API客户端"""
    def __init__(
            self,
            account: str,
            password: str,
            tenant_code: Optional[str] = None,
            baseurl: str = DEFAULT_BASEURL,
            timeout: Union[int, Tuple[int, int]] = DEFAULT_TIMEOUT,
            session: Optional[requests.Session] = None
    ):
        """
        初始化WeBan API客户端
        :param account: 账号
        :param password: 密码
        :param tenant_code: 学校代码
        :param baseurl: 基础URL
        :param timeout: 超时时间 (连接超时, 读取超时)
        :param session: 可选的requests会话
        """
        self.account = account
        self.password = password
        self.tenant_code = tenant_code
        self.baseurl = baseurl.rstrip("/")
        self.timeout = timeout
        self.session = session or SessionManager.create_retry_session(self.baseurl)
        self.user: Optional[Dict[str, Any]] = None

    @staticmethod
    def get_timestamp(int_len: int = 10, frac_len: int = 3) -> str:
        """
        获取当前时间戳
        :param int_len: 整数部分长度
        :param frac_len: 小数部分长度
        :return: 格式化的时间戳字符串
        """
        t = str(time.time_ns())
        if frac_len <= 0:
            return t[:int_len]
        return f"{t[:int_len]}.{t[int_len:int_len+frac_len]}"

    def set_tenant_code(self, tenant_code: str) -> None:
        """设置学校代码"""
        self.tenant_code = tenant_code

    def _api_request(
            self,
            endpoint: str,
            method: str = "POST",
            params: Optional[Dict[str, Any]] = None,
            data: Optional[Dict[str, Any]] = None,
            encrypt: bool = False,
            require_auth: bool = True
    ) -> APIResponse:
        """
        通用API请求方法
        :param endpoint: API端点路径
        :param method: HTTP方法 (GET/POST)
        :param params: URL参数
        :param data: 请求体数据
        :param encrypt: 是否加密请求数据
        :param require_auth: 是否需要认证
        :return: API响应对象
        """
        # 验证必要条件
        if require_auth and not self.user:
            raise AuthenticationError("需要先登录系统")
        if require_auth and not self.session.headers.get("X-Token"):
            raise AuthenticationError("认证令牌不存在，请重新登录")
        if not self.tenant_code and require_auth:
            raise ConfigurationError("学校代码(tenant_code)未设置")

        # 构建请求参数
        url = f"{self.baseurl}/{endpoint.lstrip('/')}"
        request_params = params or {}
        request_params.setdefault("timestamp", self.get_timestamp())
        request_data = data or {}

        # 加密数据（如果需要）
        if encrypt:
            request_data = {"data": CryptoUtils.encrypt(request_data)}

        try:
            # 发送请求
            logger.info(f"发送{method}请求到: {url}")
            response = self.session.request(
                method=method,
                url=url,
                params=request_params,
                data=request_data,
                timeout=self.timeout
            )
            response.raise_for_status()

            # 解析响应
            json_response = response.json()
            api_response = APIResponse.from_json(json_response)

            # 处理API错误
            if not api_response.success:
                logger.error(f"API请求失败: {api_response}")
                raise APIError(
                    message=f"API请求失败: {api_response.detail_code}",
                    code=api_response.code,
                    response=response
                )

            return api_response

        except requests.exceptions.RequestException as e:
            logger.error(f"HTTP请求异常: {str(e)}")
            raise APIError(f"网络请求失败: {str(e)}") from e
        except json.JSONDecodeError as e:
            logger.error(f"响应解析失败: {str(e)}")
            raise APIError(f"响应数据格式错误: {str(e)}") from e

    def get_tenant_list_with_letter(self) -> Dict[str, Any]:
        """获取学校代码和名称列表"""
        response = self._api_request(
            endpoint="pharos/login/getTenantListWithLetter.do",
            require_auth=False
        )
        return response.data

    def get_tenant_config(self, tenant_code: Optional[str] = None) -> Dict[str, Any]:
        """获取学校配置"""
        tenant_code = tenant_code or self.tenant_code
        if not tenant_code:
            raise ConfigurationError("学校代码(tenant_code)未提供")

        response = self._api_request(
            endpoint="pharos/login/getTenantConfig.do",
            data={"tenantCode": tenant_code},
            require_auth=False
        )
        return response.data

    def get_help(self, tenant_code: Optional[str] = None) -> Dict[str, Any]:
        """获取帮助文件"""
        tenant_code = tenant_code or self.tenant_code
        if not tenant_code:
            raise ConfigurationError("学校代码(tenant_code)未提供")

        response = self._api_request(
            endpoint="pharos/login/getHelp.do",
            data={"tenantCode": tenant_code},
            require_auth=False
        )
        return response.data

    def rand_letter_image(self, verify_time: Optional[str] = None) -> bytes:
        """获取验证码图片"""
        params = {
            "time": verify_time or self.get_timestamp(frac_len=0)
        }

        try:
            url = f"{self.baseurl}/pharos/login/randLetterImage.do"
            response = self.session.get(
                url=url,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            logger.error(f"获取验证码失败: {str(e)}")
            raise APIError(f"获取验证码图片失败: {str(e)}") from e

    def login(self, verify_code: str, verify_time: Optional[int] = None) -> Dict[str, Any]:
        """
        用户登录
        :param verify_code: 验证码
        :param verify_time: 验证码时间戳
        :return: 用户信息
        """
        if not self.tenant_code:
            raise ConfigurationError("学校代码(tenant_code)未设置")

        data = {
            "keyNumber": self.account,
            "password": self.password,
            "tenantCode": self.tenant_code,
            "time": verify_time or int(self.get_timestamp(frac_len=0)),
            "verifyCode": verify_code,
        }

        response = self._api_request(
            endpoint="pharos/login/login.do",
            data=data,
            encrypt=True,
            require_auth=False
        )

        # 存储用户信息和令牌
        user_data = response.data
        if user_data.get("token"):
            self.user = user_data
            self.session.headers["X-Token"] = user_data["token"]
            self.password = None  # 登录后清除明文密码
            logger.info(f"用户{self.account}登录成功")
        else:
            raise AuthenticationError("登录失败，未获取到认证令牌")

        return user_data

    def list_study_task(self) -> List[Dict[str, Any]]:
        """获取学习任务列表"""
        response = self._api_request(
            endpoint="pharos/index/listStudyTask.do",
            data={
                "tenantCode": self.tenant_code,
                "userId": self.user["userId"]
            }
        )
        return response.data

    def list_my_project(self, ended: int = 2) -> List[Dict[str, Any]]:
        """
        获取我的项目列表
        :param ended: 1:进行中 2:已结束
        :return: 项目列表
        """
        if ended not in [1, 2]:
            raise ValueError("ended参数必须为1(进行中)或2(已结束)")

        response = self._api_request(
            endpoint="pharos/index/listMyProject.do",
            data={
                "tenantCode": self.tenant_code,
                "userId": self.user["userId"],
                "ended": ended
            }
        )
        return response.data

    def show_progress(self, user_project_id: str) -> Dict[str, Any]:
        """
        获取学习任务进度
        :param user_project_id: 用户项目ID
        :return: 学习进度信息
        """
        if not user_project_id:
            raise ValueError("user_project_id不能为空")

        response = self._api_request(
            endpoint="pharos/project/showProgress.do",
            data={
                "userProjectId": user_project_id,
                "userId": self.user["userId"]
            }
        )
        return response.data

    def get_resource_list(self, user_project_id: str) -> List[Dict[str, Any]]:
        """
        获取资源列表
        :param user_project_id: 用户项目ID
        :return: 资源列表
        """
        if not user_project_id:
            raise ValueError("user_project_id不能为空")

        response = self._api_request(
            endpoint="pharos/project/getResourceList.do",
            data={
                "userProjectId": user_project_id,
                "userId": self.user["userId"]
            }
        )
        return response.data

    def report_study(self, resource_id: str, user_project_id: str, duration: int = 60) -> Dict[str, Any]:
        """
        上报学习进度
        :param resource_id: 资源ID
        :param user_project_id: 用户项目ID
        :param duration: 学习时长(秒)
        :return: 上报结果
        """
        if not all([resource_id, user_project_id]):
            raise ValueError("resource_id和user_project_id不能为空")

        data = {
            "resourceId": resource_id,
            "userProjectId": user_project_id,
            "userId": self.user["userId"],
            "duration": duration,
            "position": duration,
            "isComplete": 1
        }

        response = self._api_request(
            endpoint="pharos/project/reportStudy.do",
            data=data
        )
        return response.data

    def get_exam_list(self, user_project_id: str) -> List[Dict[str, Any]]:
        """
        获取考试列表
        :param user_project_id: 用户项目ID
        :return: 考试列表
        """
        if not user_project_id:
            raise ValueError("user_project_id不能为空")

        response = self._api_request(
            endpoint="pharos/exam/getExamList.do",
            data={
                "userProjectId": user_project_id,
                "userId": self.user["userId"]
            }
        )
        return response.data

    def start_exam(self, exam_id: str, user_project_id: str) -> Dict[str, Any]:
        """
        开始考试
        :param exam_id: 考试ID
        :param user_project_id: 用户项目ID
        :return: 考试信息
        """
        if not all([exam_id, user_project_id]):
            raise ValueError("exam_id和user_project_id不能为空")

        response = self._api_request(
            endpoint="pharos/exam/startExam.do",
            data={
                "examId": exam_id,
                "userProjectId": user_project_id,
                "userId": self.user["userId"]
            }
        )
        return response.data

    def submit_exam(self, exam_record_id: str, answers: Dict[str, str]) -> Dict[str, Any]:
        """
        提交考试答案
        :param exam_record_id: 考试记录ID
        :param answers: 答案字典，格式: {questionId: answer}
        :return: 提交结果
        """
        if not all([exam_record_id, answers]):
            raise ValueError("exam_record_id和answers不能为空")

        data = {
            "examRecordId": exam_record_id,
            "userId": self.user["userId"],
            "answers": json.dumps(answers, separators=(",", ":"))
        }

        response = self._api_request(
            endpoint="pharos/exam/submitExam.do",
            data=data
        )
        return response.data

    def get_exam_result(self, exam_record_id: str) -> Dict[str, Any]:
        """
        获取考试结果
        :param exam_record_id: 考试记录ID
        :return: 考试结果
        """
        if not exam_record_id:
            raise ValueError("exam_record_id不能为空")

        response = self._api_request(
            endpoint="pharos/exam/getExamResult.do",
            data={
                "examRecordId": exam_record_id,
                "userId": self.user["userId"]
            }
        )
        return response.data

    def get_certificate(self, user_project_id: str) -> Dict[str, Any]:
        """
        获取证书
        :param user_project_id: 用户项目ID
        :return: 证书信息
        """
        if not user_project_id:
            raise ValueError("user_project_id不能为空")

        response = self._api_request(
            endpoint="pharos/certificate/getCertificate.do",
            data={
                "userProjectId": user_project_id,
                "userId": self.user["userId"]
            }
        )
        return response.data

    def get_notice_list(self) -> List[Dict[str, Any]]:
        """获取通知列表"""
        response = self._api_request(
            endpoint="pharos/index/getNoticeList.do",
            data={"userId": self.user["userId"]}
        )
        return response.data

    def get_news_list(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        获取资讯列表
        :param page: 页码
        :param page_size: 每页条数
        :return: 资讯列表及分页信息
        """
        response = self._api_request(
            endpoint="pharos/index/getNewsList.do",
            data={
                "userId": self.user["userId"],
                "page": page,
                "pageSize": page_size
            }
        )
        return response.data

    def get_user_info(self) -> Dict[str, Any]:
        """获取用户信息"""
        response = self._api_request(
            endpoint="pharos/user/getUserInfo.do",
            data={"userId": self.user["userId"]}
        )
        return response.data

    def logout(self) -> None:
        """退出登录"""
        try:
            if self.user and self.session.headers.get("X-Token"):
                self._api_request(
                    endpoint="pharos/login/logout.do",
                    data={"userId": self.user["userId"]}
                )
                logger.info(f"用户{self.account}退出登录成功")
        except Exception as e:
            logger.warning(f"退出登录时发生错误: {str(e)}")
        finally:
            self.user = None
            self.session.headers.pop("X-Token", None)
            self.session.close()

    def __enter__(self) -> 'WeBanAPI':
        """上下文管理器入口"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """上下文管理器出口，确保退出登录"""
        self.logout()