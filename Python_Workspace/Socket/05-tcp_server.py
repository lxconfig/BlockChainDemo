import socket

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip和port
    server_addr = ("", 53799)
    tcp_socket.bind(server_addr)

    # 将套接字从主动变为被动(设置为被动监听模式)
    tcp_socket.listen(128)

    while True:
        # 等待客户端连接
        # accept()返回一个元组
        # client_socket: 用于和客户端收发数据的套接字
        # client_addr: 客户端的ip和port
        # 默认阻塞，直到有客户端链接
        client_socket, client_addr = tcp_socket.accept()
        # print(client_socket, client_addr)
        while True:
            # 接收数据
            print("为客户端%s服务中..." % str(client_addr))
            recv_data = client_socket.recv(1024)
            print(recv_data.decode("GBK"))
            # recv也会堵塞，两种情况会解堵塞: 收到数据或客户端调用close
            if recv_data:
                # 返回应答
                client_socket.send("---ok---".encode("GBK"))
            else:
                break

        # 关闭套接字
        client_socket.close()
        print("为客户端%s服务完成" % str(client_addr))
    tcp_socket.close()


if __name__ == "__main__":
    main()