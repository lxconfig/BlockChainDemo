# -*- coding:utf-8 -*-
# time: 2019/05/24 10:29
# File: 02-数字签名.py
import rsa


# 生成一对公私钥

message = "hello world"

with open("genesus_private.pem", "r") as f:
    pribkey = rsa.PrivateKey.load_pkcs1(f.read().encode())


with open("genesus_public.pem", "r") as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())


# 私钥签名
signature = rsa.sign(message.encode(), pribkey, "SHA-256")

# 公钥验证
try:
    rsa.verify(message.encode(), signature, pubkey)
    print("valid")
except rsa.pkcs1.VerificationError:
    print("invalid")
