from pathlib import Path

import yaml
from loguru import logger

from .model import ConfigModel


def find_config(filename="config.yaml"):
    """递归查找配置文件"""
    current_dir = Path.cwd().resolve()

    # 使用 rglob 递归搜索所有子目录
    for path in current_dir.rglob(filename):
        if path.is_file():
            return path

    return None


def load_config() -> ConfigModel:
    config_path = find_config("config.release.yaml")
    try:
        if not config_path:
            logger.error("未找到配置文件")
            exit()

        with open(config_path, "r", encoding="utf-8") as f:
            _config = yaml.load(f, Loader=yaml.FullLoader)
            config = ConfigModel(**_config)
            logger.success("加载配置成功")
            return config
    except Exception as e:
        logger.error(f"读取配置文件失败,{e}")
        exit()


config: ConfigModel = load_config()
if __name__ == "__main__":
    logger.info(config)
