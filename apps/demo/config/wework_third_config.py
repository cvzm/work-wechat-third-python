
"""
    企业微信，第三方平台相关配置
"""

# ------- 临时配置
# TODO 此处 suiteTicket 需要等回调刷新，正常是从redis拿。
suiteTicket: str = ''


# ------- 基础配置
suiteId = ""
suiteSecret = ""
token = ""
encodingAESKey = ""


# ------- third api
baseUrl = "https://qyapi.weixin.qq.com/cgi-bin/"
serviceUrl = baseUrl + "service/"
suiteTokenUrl = serviceUrl + "get_suite_token"
# preAuthCodeUrl = serviceUrl + "get_pre_auth_code?suite_access_token=%s"
# permanentCodeUrl = serviceUrl + "get_permanent_code?suite_access_token=%s"
# sessionInfoUrl = serviceUrl + "set_session_info?suite_access_token=%s"


