# -*- coding:utf-8 -*-
# time: 2019/05/04 15:27
# File: tcp_client.py
import socket

def main():
    '''tcp客户端'''
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(("10.21.21.119", 8080))
    # 发送数据
    data = input("请输入发送的内容：")
    tcp_socket.send(data.encode("GBK"))
    # 接收数据
    recv_data = tcp_socket.recvfrom(1024)
    print(recv_data[0].decode("GBK"))
    # 关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()