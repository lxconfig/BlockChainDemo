import socket


def main():
    """
        写一个TCP服务器，然后让浏览器充当客户端，访问服务器的资源(简单返回一个固定页面)
    """
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 即使服务器被强制关闭，再次运行不会报错，地址可以再次使用
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定ip和port
    server_addr = ('', 53799)
    tcp_socket.bind(server_addr)

    # 将套接字由主动转为被动
    tcp_socket.listen(128)

    while True:
        # 等待客户端的连接
        client_socket, client_addr = tcp_socket.accept()

        # 接收客户端发送的请求数据
        request_data = client_socket.recv(1024)
        print(request_data)
        print(client_addr)

        # 根据请求数据返回页面
        # windows中\r\n表示换行
        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n<h1>ok</h1>'
        # response += '<h1>ok</h1>'
        client_socket.send(response.encode("utf-8"))
        
        # 关闭套接字
        client_socket.close()
    tcp_socket.close()


if __name__ == "__main__":
    main()