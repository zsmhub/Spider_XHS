import os
import json
import random
from loguru import logger
from dotenv import load_dotenv

def get_cookies():
    load_dotenv()
    cookies_str = os.getenv('COOKIES')

    # 尝试解析为 JSON 数组
    if cookies_str:
        try:
            cookies_array = json.loads(cookies_str)
            if isinstance(cookies_array, list) and len(cookies_array) > 0:
                # 随机选择一个 cookie
                selected_cookie = random.choice(cookies_array)
                logger.info(f'从 {len(cookies_array)} 个 cookies 中随机选择了一个: {selected_cookie[-6:]}')
                return selected_cookie
            else:
                logger.warning('COOKIES 环境变量不是有效的数组格式，使用原始字符串')
                return cookies_str
        except json.JSONDecodeError:
            logger.warning('COOKIES 环境变量不是有效的 JSON 格式，使用原始字符串')
            return cookies_str

    return cookies_str

def init():
    media_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../datas/media_datas'))
    excel_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../datas/excel_datas'))
    for base_path in [media_base_path, excel_base_path]:
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            logger.info(f'创建目录 {base_path}')
    base_path = {
        'media': media_base_path,
        'excel': excel_base_path,
    }
    return base_path
