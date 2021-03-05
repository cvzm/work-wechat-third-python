import hashlib

from apps.demo.utils import aes_exception
from apps.demo.utils.aes_exception import AesException


class SHA1:
    """计算消息签名"""

    def get_SHA1(self, token, timestamp, nonce, encrypt) -> str:
        """用SHA1算法生成安全签名
        @param token:  票据
        @param timestamp: 时间戳
        @param encrypt: 密文
        @param nonce: 随机字符串
        @return: 安全签名
        """
        try:
            sort_list = [token, timestamp, nonce, encrypt]
            sort_list.sort()
            print(sort_list)
            sha = hashlib.sha1()
            sha.update(''.join(sort_list).encode('utf-8'))
            return sha.hexdigest()
        except Exception as e:
            print(e)
            raise AesException(aes_exception.ComputeSignatureError)

