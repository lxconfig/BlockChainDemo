import socket

def Send(udp_socket):
    send_data = input("请输入要发送的内容:")
    udp_socket.sendto(send_data.encode('utf-8'), ("192.168.1.4", 8080))

def Recv(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    send_addr = recv_data[1]
    recv_msg = recv_data[0].decode("GBK")
    print("%s:%s" % (str(send_addr), recv_msg))

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定ip和port
    local_addr = ("", 54377)
    udp_socket.bind(local_addr)

    while True:
        # 发送数据
        Send(udp_socket)

        # 接收数据
        Recv(udp_socket)

    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()