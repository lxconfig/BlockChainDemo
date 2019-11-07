# -*- coding:utf-8 -*-
# time: 2019/04/29 14:49
# File: udp_sendto_by_same_socket.py
import socket

# 创建socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定port
local_addr = ('', 7788)
udp_socket.bind(local_addr)

# 发送数据
send_data = input("请输入发送数据：")
dest_addr = ('10.21.21.119', 8080)
udp_socket.sendto(send_data.encode("GBK"), dest_addr)

# 接受数据
recv_data = udp_socket.recvfrom(1024)
recv_msg = recv_data[0].decode('GBK')  # 接收到的数据
send_addr_ip = recv_data[1][0]  # 发送方ip
send_addr_port = recv_data[1][1]  # 发送方port
send_addr = str(send_addr_ip) + ":" + str(send_addr_port)  # 发送方地址

# 打印数据
print(send_addr + "\n", recv_msg)
# 关闭socket
udp_socket.close()