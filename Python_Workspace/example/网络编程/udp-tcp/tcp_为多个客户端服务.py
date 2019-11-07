# -*- coding:utf-8 -*-
# time: 2019/05/04 19:46
# File: 为多个客户端服务.py
import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    while True:
        print("等待一个客户端链接中...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端%s已经链接" % str(client_addr))
        while True:
            recv_data = new_client_socket.recv(1024)
            print("客户端发送的数据是：%s" % recv_data.decode("GBK"))
            # 如果recv解堵塞，那么2种情况：
            # 1.客户端发送数据
            # 2.客户端调用close
            if recv_data:
                new_client_socket.send("服务结束！".encode("GBK"))
            else:
                break
        new_client_socket.close()
        print("已经服务完毕")
    tcp_server_socket.close()




if __name__ == '__main__':
    main()