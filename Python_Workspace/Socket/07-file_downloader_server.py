import socket

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip和port
    server_addr = ("192.168.1.4", 53799)
    tcp_socket.bind(server_addr)

    # 改为被动监听模式
    tcp_socket.listen(128)

    # 等待客户端连接
    client_socket, client_addr = tcp_socket.accept()

    # 接收客户端发来的文件名
    file_name = client_socket.recv(1024).decode('utf-8')
    print("客户端%s需要下载的文件是: %s" % (str(client_addr), file_name))

    # 打开文件，读取数据
    file_content = None
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as e:
        print(e)
        print("没有要下载的文件(%s)" % file_name)

    # 发送给客户端
    if file_content:
        client_socket.send(file_content)

    # 关闭套接字
    client_socket.close()
    tcp_socket.close()

if __name__ == "__main__":
    main()