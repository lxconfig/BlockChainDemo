# -*- coding:UTF-8 -*-
# time: 2019/05/05 15:05
# File: 案例-文件下载器-client.py
import socket

def main():
    # 1.创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.连接服务器
    tcp_client_socket.connect(("10.21.21.119", 7890))
    # 3.发送要下载的文件名给服务器
    file_name = input("请输入要下载的文件名：")
    tcp_client_socket.send(file_name.encode("GBK"))
    # 4.接收服务器返回的文件内容
    file_content = tcp_client_socket.recv(1024)
    # 5.将收到的内容写入文件中
    if file_content:
        with open("[新]"+ file_name, "wb") as f:
            f.write(file_content)
    else:
        print("下载失败！服务器中没有%s这个文件，请检查文件名后再试" % file_name)
    # 6.关闭套接字
    tcp_client_socket.close()

if __name__ == '__main__':
    main()