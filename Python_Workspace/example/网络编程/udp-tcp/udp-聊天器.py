# -*- coding:utf-8 -*-
# time: 2019/04/29 15:46
# File: udp-聊天器.py
import socket

def send_data(udp_socket):
    '''发送数据'''
    dest_addr = ("10.21.21.119", 8080)
    content = input("请输入发送内容：")
    udp_socket.sendto(content.encode("GBK"), dest_addr)


def recv_data(udp_socket):
    '''接收数据'''
    recv_content = udp_socket.recvfrom(1024)
    print(recv_content[0].decode("GBK"))


def main():
    '''主函数用来创建socket'''
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建socket
    local_addr = ("", 7788)
    udp_socket.bind(local_addr)
    while True:
        send_data(udp_socket)
        recv_data(udp_socket)

if __name__ == '__main__':
    main()