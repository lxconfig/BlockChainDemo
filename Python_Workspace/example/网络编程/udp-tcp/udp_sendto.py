# -*- coding:utf-8 -*-
# time: 2019/04/24 19:34
# File: udp_demo.py
import datetime
import socket
start = datetime.datetime.now()
# 创建socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
local_addr = ('', 7789)
udp_socket.bind(local_addr)
while True:
    # 从键盘获取数据
    send_data = input("请输入发送的数据：")
    if send_data == "exit":
        break # continue只是退出本次循环
    # 使用socket
    # udp_socket.sendto(b"nihao", ("10.21.21.119", 8080))
    udp_socket.sendto(send_data.encode("GBK"), ("10.21.21.119", 8080))
# 关闭socket
udp_socket.close()

end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")