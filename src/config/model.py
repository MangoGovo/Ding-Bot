from pydantic import BaseModel


class Dingtalk(BaseModel):
    """钉钉相关配置"""

    client_id: str
    client_secret: str


class WPSExcel(BaseModel):
    """WPS在线文档相关配置"""

    # 分享链接
    share_url: str
    # cookie中的sid参数
    sid: str


class ConfigModel(BaseModel):
    dingtalk: Dingtalk
    wps_excel: WPSExcel
