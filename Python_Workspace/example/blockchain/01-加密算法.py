# -*- coding:utf-8 -*-
# time: 2019/05/24 9:56
# File: 01-加密算法.py
import rsa


def create_genisus_keypair():
    """生成公私钥"""
    pubkey, privkey = rsa.newkeys(1024)
    with open("genisus_public.pem", "w+") as f:
        f.write(pubkey.save_pkcs1().decode())

    with open("genisus_private.pem", "w+") as f:
        f.write(privkey.save_pkcs1().decode())


# 导入密钥
with open("genesus_private.pem", "r") as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

with open("genesus_public.pem", "r") as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

# 明文
message = "hello world"

# 公钥加密
crypto = rsa.encrypt(message.encode(), pubkey)

# 私钥解密
message = rsa.decrypt(crypto, privkey).decode()
print(message)

if __name__ == '__main__':
    create_genisus_keypair()
