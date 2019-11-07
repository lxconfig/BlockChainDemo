# -*- coding:utf-8 -*-
# time: 2019/04/26 14:44
# File: udp_recv_data.py
import socket
def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)
    while True:
        # 接收数据
        recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        recv_msg = recv_data[0].decode('GBK')  # 接收到的数据
        send_addr_ip = recv_data[1][0]  # 发送方ip
        send_addr_port = recv_data[1][1]  # 发送方port
        send_addr = str(send_addr_ip) + ":" + str(send_addr_port)  # 发送方地址
        # 打印数据
        print(send_addr + "\n", recv_msg)
    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()