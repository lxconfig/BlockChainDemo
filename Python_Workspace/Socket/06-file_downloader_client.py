import socket

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 链接服务器
    server_addr = ("192.168.1.4", 53799)
    tcp_socket.connect(server_addr)

    # 发送需要下载的文件
    file_name = input("请输入需要下载的文件名:")
    tcp_socket.send(file_name.encode("utf-8"))

    # 接收服务器返回的文件内容，保存在新文件中
    recv_data = tcp_socket.recv(1024)
    if recv_data:
        with open("[新]"+file_name, 'wb') as f:
            f.write(recv_data)

    # 关闭套接字
    tcp_socket.close()

if __name__ == "__main__":
    main()