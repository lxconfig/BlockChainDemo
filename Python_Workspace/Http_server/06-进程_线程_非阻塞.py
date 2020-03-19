import socket


def main():
    '''
        用套接字的非阻塞模式实现单个进程或线程为多个客户端服务
    '''
    client_socket_list = list()
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('', 7890))
    tcp_socket.listen(128)

    # 将套接字改为非阻塞模式(accept,recv不堵塞，没有客户端连接或发送数据就发生异常)
    tcp_socket.setblocking(False)

    while True:
        try:
            client_socket, client_addr = tcp_socket.accept()
        except Exception as ret:
            # 没有客户端连接就发生异常
            print("没有新的客户端连接", ret)
        else:
            print("有新的客户端连接", client_addr)
            # 将为这个客户端服务的套接字也改为非阻塞模式
            client_socket.setblocking(False)
            client_socket_list.append(client_socket)
    
    for client_s in client_socket_list:
        try:
            data = client_s.recv()
        except Exception as ret:
            # 客户端没有发送数据就发生异常
            print("客户端没有发送数据", ret)
        else:
            print("客户端发送了数据", data)



if __name__ == "__main__":
    main()