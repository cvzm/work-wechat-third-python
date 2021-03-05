
"""
    企业微信 Aes相关异常
"""


ValidateSignatureError = -40001
ParseXmlError = -40002
ComputeSignatureError = -40003
IllegalAesKey = -40004
ValidateCorpidError = -40005
EncryptAESError = -40006
DecryptAESError = -40007
IllegalBuffer = -40008


def get_message(code: int) -> str:
    if code == ValidateSignatureError:
        return '签名验证错误'
    if code == ParseXmlError:
        return 'xml解析失败'
    if code == ComputeSignatureError:
        return 'sha加密生成签名失败'
    if code == IllegalAesKey:
        return 'SymmetricKey非法'
    if code == ValidateCorpidError:
        return 'corpid校验失败'
    if code == EncryptAESError:
        return 'aes加密失败'
    if code == DecryptAESError:
        return 'aes解密失败'
    if code == IllegalBuffer:
        return '解密后得到的buffer非法'


class AesException(Exception):
    """ 认证异常 """
    code: int
    msg: str

    def __init__(self, code: int):
        self.code = code
        self.msg = get_message(code)

