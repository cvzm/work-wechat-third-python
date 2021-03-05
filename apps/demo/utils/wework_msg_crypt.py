from apps.demo.utils import aes_exception
from apps.demo.utils.aes_exception import AesException
from apps.demo.utils.aes_utils import AES_CBC
from apps.demo.utils.sha1 import SHA1
from apps.demo.utils.xml_utils import xml_get_value
import base64


class WeWorkMsgCrypt:
    """
        提供接收和推送给企业微信消息的加解密
    """
    def __init__(self, token: str, encoding_aes_key: str):
        """
        :param token: 企业微信token
        :param encoding_aes_key: 企业微信EncodingAESKey
        """
        self.token = token
        self.encoding_aes_key = base64.b64decode(encoding_aes_key + "=")

    def decrypt_msg(self, msg_signature: str, time_stamp: str, nonce: str, post_data: str) -> str:
        """ 检验消息的真实性，并且获取解密后的明文.
        @param msg_signature: 签名串，对应URL参数的 msg_signature
        @param time_stamp: 时间戳，对应URL参数的timestamp
        @param nonce: 随机串，对应URL参数的nonce
        @param post_data: 密文，对应POST请求的数据
        @return 解密后的原文
        """
        encrypt = xml_get_value(post_data, 'Encrypt')
        # 校验信息
        signature = SHA1().get_SHA1(self.token, time_stamp, nonce, encrypt)
        if signature is '' or signature != msg_signature:
            raise AesException(aes_exception.ValidateSignatureError)

        # 解密
        return AES_CBC().decrypt_oracle(self.encoding_aes_key, encrypt)
