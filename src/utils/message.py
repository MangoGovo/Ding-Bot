import io

import pandas as pd
import requests
from loguru import logger

from config.loader import config


def load_msg():
    """加载机器人回复内容到本地内存"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    }
    cookies = {"wps_sid": config.wps_excel.sid}
    url = config.wps_excel.share_url
    # 获取下载链接
    response = requests.get(url, headers=headers, cookies=cookies)
    url = response.json()["download_url"]
    # 下载表格
    response = requests.get(url)
    binary_data = io.BytesIO(response.content)
    # 解析表格
    df = pd.read_excel(binary_data, sheet_name="release")
    botmsg = {}
    for _, row in df.iterrows():
        key = row.iloc[0]
        value = row.iloc[1]
        if key in botmsg:
            logger.error(f"key {key} 重复")
        botmsg[key] = value

    logger.info(f"botmsg 关键字加载完毕，共 {len(botmsg)} 条数据")
    return botmsg


botmsg = load_msg()
