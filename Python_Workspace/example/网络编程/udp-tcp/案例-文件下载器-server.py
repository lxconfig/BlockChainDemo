# -*- coding:UTF-8 -*-
# time: 2019/05/05 15:13
# File: 案例-文件下载器-server.py
import socket

def send_file_2_client(file_name, client_socket):
    # 6.读取该文件中的内容
    file_content = None
    try:
        with open(file_name, 'rb') as f:
            file_content = f.read()
    except Exception as ret:
        print("抱歉!服务器中未找到文件：%s" % file_name)
    # 7.发送文件内容给客户端
    if file_content:
        client_socket.send(file_content)
        print("%s下载完成！" % file_name)
    else:
        client_socket.send(''.encode("GBK"))

def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定ip和port
    tcp_server_socket.bind(("", 7890))
    # 3.将套接字改为被动监听状态
    tcp_server_socket.listen(128)
    while True:
        # 4.等待客户端链接
        print("等待客户端链接中...")
        client_socket, client_addr = tcp_server_socket.accept()
        print("客户端%s成功链接!" % str(client_addr))
        # 5.接收客户端发送的文件名
        file_name = client_socket.recv(1024).decode("GBK")
        print("客户端%s需要的文件是：%s" % (client_addr, file_name))
        # 调用发送数据的函数
        send_file_2_client(file_name, client_socket)
        # 8.关闭套接字
        client_socket.close()
    tcp_server_socket.close()

if __name__ == '__main__':
    main()