# -*- coding:utf-8 -*-
# time: 2019/05/07 21:02
# File: 多任务udp聊天器.py
import socket
import threading

def send(udp_socket):
    while True:
        # 3.发送数据
        send_msg = input("请输入要发送的消息：")
        udp_socket.sendto(send_msg.encode("GBK"), ("10.21.21.119", 8080))

def recv(udp_socket):
    while True:
        # 4.接收数据
        recv_msg = udp_socket.recvfrom(1024)
        print(recv_msg[0].decode("GBK"))

def main():
    """主函数控制整体流程"""
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定本地信息 ip和port
    local_addr = (("", 7890))
    udp_socket.bind(local_addr)
    # 创建线程
    t_send = threading.Thread(target=send, args=(udp_socket,))
    t_recv = threading.Thread(target=recv, args=(udp_socket,))
    # 启动线程
    t_send.start()
    t_recv.start()

if __name__ == '__main__':
    main()