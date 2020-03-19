import socket
import threading


def recv_msg(udp_socket):
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data[0].decode("GBK"))   


def send_msg(udp_socket):
    # 发送数据
    while True:
        send_data = input("请输入要发送的信息:")
        udp_socket.sendto(send_data.encode("GBK"), ("192.168.1.4", 8080))


def main():
    """多任务版udp聊天器"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定ip和port
    local_addr = ("", 53799)
    udp_socket.bind(local_addr)
    
    # 创建线程，实现同时收发数据
    recv_thread = threading.Thread(target=recv_msg, args=(udp_socket,))
    send_thread = threading.Thread(target=send_msg, args=(udp_socket,))

    # 启动线程
    recv_thread.start()
    send_thread.start()

    # 不能在这里关闭套接字，不然会报错：在一个非套接字上尝试了一个操作
    # 原因: 没有sleep，启动完两个子线程后，主线程继续执行，关闭套接字，导致两个任务函数无法执行
    # 关闭套接字
    # udp_socket.close()

if __name__ == "__main__":
    main()