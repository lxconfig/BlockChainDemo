import socket

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定程序ip和port ""表示本机任意ip
    local_addr = ("", 54377)
    udp_socket.bind(local_addr)

    while True:
        # 接收数据
        # 1024表示接收数据的最大值
        recv_data = udp_socket.recvfrom(1024)
        if recv_data[0].decode('GBK') == "exit":
            break
        # 显示数据
        # recv_data是一个元组 (b'\xc4\xe3\xba\xc3', ('192.168.1.4', 8080))
        # 包含数据和发件人ip port
        # windows的中文字符使用的是GBK编码
        # print(recv_data[0].decode('GBK'))
        print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("GBK")))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()