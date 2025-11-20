import json
import sys
import traceback
from loguru import logger
from typing import List, Dict, Tuple, Optional

from client import WeBanClient


class ConfigLoader:
    """配置加载器，处理配置文件的加载和验证"""
    @staticmethod
    def load_config(config_path: str = 'config.json') -> Tuple[List[Dict], bool, int]:
        """
        加载并验证配置文件
        :param config_path: 配置文件路径
        :return: (用户列表, 是否学习, 学习时长)
        :raises: FileNotFoundError, JSONDecodeError, ValueError
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                if not isinstance(config, dict):
                    raise ValueError("配置文件格式错误，顶层应为字典结构")

            users = config.get('users', [])
            if not isinstance(users, list):
                raise ValueError("配置文件中users必须是列表")

            # 验证用户配置
            for user in users:
                if not isinstance(user, dict):
                    raise ValueError("用户配置必须是字典")
                required_keys = ['account', 'password', 'school']
                for key in required_keys:
                    if key not in user:
                        raise ValueError(f"用户配置缺少必要字段: {key}")

            study = config.get('study', True)
            study_time = config.get('study_time', 15)  # 默认值从15分钟改为15秒

            # 修改学习时长验证提示
            if not isinstance(study_time, int) or study_time <= 0:
                raise ValueError(f"学习时长(秒)必须是正整数，当前值: {study_time}")

            return users, study, study_time

        except FileNotFoundError:
            logger.error(f"配置文件 {config_path} 不存在，请复制 config.example.json 并修改")
            sys.exit(1)
        except json.JSONDecodeError:
            logger.error("配置文件格式错误，请检查JSON语法")
            sys.exit(1)
        except ValueError as e:
            logger.error(f"配置文件内容错误: {e}")
            sys.exit(1)


def process_user(user: Dict, study: bool = True, study_time: int = 15) -> bool:
    """
    处理单个用户的学习任务
    :param user: 用户配置
    :param study: 是否执行学习任务
    :param study_time: 学习时长(秒)  # 单位从分钟改为秒
    :return: 任务是否成功
    """
    account = user.get('account', '未知账号')
    try:
        client = WeBanClient(
            account=user['account'],
            password=user['password'],
            school=user['school'],
            study_time=study_time  # 已调整为秒单位
        )
        logger.info(f"[{account}] 开始执行任务")

        # 获取验证码
        verify_time, captcha_image = client.get_verify_code()
        verify_code = client.ocr.classification(captcha_image) if client.ocr else \
                      input(f"请输入[{user['account']}]的验证码: ")

        # 登录
        login_success, error_msg = client.login(verify_code, verify_time)
        if not login_success:
            logger.error(f"[{account}] 登录失败: {error_msg}")
            return False

        # 执行学习
        if study:
            if not client.run_study():
                logger.error(f"[{account}] 学习任务失败")
                return False

        # 同步答案
        if not client.sync_answers():
            logger.error(f"[{account}] 同步答案失败")
            return False

        logger.success(f"[{account}] 任务完成")
        return True

    except Exception as e:
        logger.error(f"[{account}] 运行失败: {str(e)}")
        traceback.print_exc()
        return False


def run_weban_task(school: str, username: str, password: str, study_time: int = 15) -> bool:
    """
    执行单个用户的Weban任务(供GUI调用)
    :param school: 学校名称
    :param username: 用户名
    :param password: 密码
    :param study_time: 学习时长(秒)  # 单位从分钟改为秒
    :return: 是否成功
    """
    user = {
        'account': username,
        'password': password,
        'school': school
    }
    return process_user(user, study=True, study_time=study_time)


def main() -> None:
    """主入口函数"""
    users, study, study_time = ConfigLoader.load_config()
    logger.info(f"开始执行，共加载到 {len(users)} 个账号")

    for user in users:
        process_user(user, study, study_time)

    input("按回车键退出")


if __name__ == "__main__":
    main()
