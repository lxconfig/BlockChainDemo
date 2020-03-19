import socket

def main():
    # 创建udp_socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # 使用套接字发送数据
        # 注: 
        # 1. 发送的字符必须是字节形式 b"hhhh"/send_data.encode("utf-8")
        # 2. 网络必须可达
        send_data = input("请输入:")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.1.4", 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()