# -*- coding:utf-8 -*-
# time: 2019/05/04 18:56
# File: tcp_server.py
import socket

def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定ip和port
    tcp_server_socket.bind(("", 7788))

    # 3.让默认的套接字由主动变被动 listen
    tcp_server_socket.listen(128)

    # 4.等待客户端的链接 accept
    new_client_socket, client_addr = tcp_server_socket.accept()
    
    # 接收客户端发送的数据
    recv_data = new_client_socket.recv(1024)
    print(recv_data.decode("GBK"))
    
    # 发送数据给客户端
    new_client_socket.send("你好！".encode("GBK"))
    
    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()
    



if __name__ == '__main__':
    main()