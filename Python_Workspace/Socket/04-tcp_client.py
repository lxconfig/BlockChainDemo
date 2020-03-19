import socket

def main():
    # 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    server_addr = ("192.168.1.4", 8080)
    tcp_socket.connect(server_addr)

    while True:
        # 发送数据
        send_data = input("请输入要发送的消息:")
        if send_data == "exit":
            break
        tcp_socket.send(send_data.encode('GBK'))

    # 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()