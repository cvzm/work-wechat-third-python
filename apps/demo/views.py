from django.shortcuts import render


from django.http import HttpResponse

from apps.demo.config import wework_third_config
from apps.demo.utils.wework_msg_crypt import WeWorkMsgCrypt
from apps.demo.utils.xml_utils import xml_get_value
import requests


def index(request):
    return HttpResponse("This is work-wechat-third-python.")


# -------- 回调相关

# 回调接口
def callback_instruct(request):
    msg_signature = request.GET.get('msg_signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')

    # 解密信息
    crypt = WeWorkMsgCrypt(wework_third_config.token, wework_third_config.encodingAESKey)
    msg = crypt.decrypt_msg(msg_signature, timestamp, nonce, request.body)

    # 根据info_type，做不同操作
    info_type = xml_get_value(msg, 'InfoType')
    if info_type == 'suite_ticket':
        # TODO Redis Add suite_ticket
        suite_ticket = xml_get_value(msg, 'SuiteTicket')
        print(suite_ticket)
        wework_third_config.suiteTicket = suite_ticket

    return HttpResponse("success")


# ------- WeChat work service api

def get_suite_token(request):
    """ 获取第三方应用凭证 demo
    官方api: https://open.work.weixin.qq.com/api/doc/90001/90143/90600
    """
    param = {
        'suite_id': wework_third_config.suiteId,
        'suite_secret': wework_third_config.suiteSecret,
        'suite_ticket': wework_third_config.suiteTicket,
    }
    resp = requests.post(wework_third_config.suiteTokenUrl, json=param)
    print(resp.json())
    return HttpResponse(resp.json().get('suite_access_token'))




