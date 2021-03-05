import base64
from Crypto.Cipher import AES
import socket
import struct


'''
AES AES/CBC/PKCS5|Zero
采用AES对称加密算法
    在PKCS5Padding中，明确定义Block的大小是8位
    而在PKCS7Padding定义中，对于块的大小是不确定的，可以在1-255之间
    PKCS #7 填充字符串由一个字节序列组成，每个字节填充该字节序列的长度。
    假定块长度为 8，数据长度为 9，
    数据： FF FF FF FF FF FF FF FF FF
    PKCS7 填充： FF FF FF FF FF FF FF FF FF 01 01 01 01 01 01 01   ?应该是填充01
    
    python3:填充bytes(这个说法不对,AES的参数是字符串,不是byte)
    length = 16 - (len(data) % 16)
    data += bytes([length])*length
 
    python2:填充字符串
    length = 16 - (len(data) % 16)
    data += chr(length)*length
    
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s : s[0:-ord(s[-1])]
'''


class AES_CBC:

    # 偏移量 16个0
    iv = "0000000000000000"

    def add_to_16(self, value):
        while len(value) % 16 != 0:
            value += '\0'
        return str.encode(value)  # 返回bytes

    # 加密方法
    def encrypt_oracle(self, key, text):
        # 初始化加密器
        aes = AES.new(key, AES.MODE_CBC, self.add_to_16(self.iv))
        bs = AES.block_size
        pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)  # PKS7

        encrypt_aes = aes.encrypt(str.encode(pad2(text)))
        # 用base64转成字符串形式
        # 执行加密并转码返回bytes
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
        return encrypted_text

    # 解密方法
    def decrypt_oracle(self, key, text):
        aes = AES.new(key, AES.MODE_CBC, self.add_to_16(self.iv))
        # 执行解密密并转码
        decrypted_text = aes.decrypt(base64.b64decode(text))
        # 去除偏移量字符
        content = decrypted_text[16: -decrypted_text[-1]]
        xml_len = socket.ntohl(struct.unpack("I", content[:4])[0])
        xml_content = content[4: xml_len+4]
        return xml_content
