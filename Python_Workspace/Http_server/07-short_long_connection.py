import socket
import re


'''
    1. 长连接
        - 指的是客户端连接上服务器，请求并得到某资源后，并没有关闭套接字(四次挥手)，可以继续使用该套接字继续请求资源(HTTP 1.1 默认是长连接)
    
    2. 短连接
        - 与长连接相反，请求并得到该资源后，关闭套接字。还要请求资源的话，要重新建立连接(三次握手 请求数据 四次挥手)

    3. 如何让浏览器知道服务器已经发送完了？
        - 在响应头中添加 Content-Length:x 字段
'''


def service_client(client_socket, request_data):
        # 把请求信息切割，得到一个列表
        data_lines = request_data.splitlines()
        # print(data_lines)

        # 使用正则，提取请求的文件名
        # GET /info.html HTTP/1.1
        # [^ ]表示非空，[]搭配^可以表示取反操作
        try:
            ret = re.match(r"[^/]+/([^ ]*)", data_lines[0]).group(1)
            if ret:
                file_name = ret
            else:
                file_name = 'info.html'
        except Exception:
            file_name = 'info.html'

        # 根据文件名读取数据
        print(file_name)
        try:
            with open("./html/"+file_name, "rb") as f:
                file_content = f.read()
        except Exception as e:
            print(e)
            # 文件不存在返回404
            response_body = "\r\n File Not Found!"
            response_header = 'HTTP/1.1 404 NOT FOUND\r\n'
            response_header += "Content-Length:%d\r\n" % len(response_body)
            response_header += "\r\n"
            response = response_header + response_body
            client_socket.send(response.encode("utf-8"))
        else:
            # 根据请求数据返回页面
            # windows中\r\n表示换行
            response_body = file_content
            response_header = 'HTTP/1.1 200 OK\r\n'
            # 响应头中的Content-Length字段可以表示是否发送完毕
            response_header += "Content-Length:%d\r\n" % len(response_body)
            response_header += "\r\n"
            response = response_header.encode('utf-8') + response_body
            # 返回响应
            client_socket.send(response)
        
        # 关闭套接字
        # 此时关闭的话就是短连接
        # client_socket.close()

def main():
    """
        单进程、单线程，长连接实现http服务器
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

    # 将套接字改为非阻塞模式
    tcp_socket.setblocking(False)
    socket_list = list()
    while True:
        # 等待客户端的连接
        try:
            client_socket, _ = tcp_socket.accept()
        except Exception:
            pass
        else:
            # 有客户端连接
            client_socket.setblocking(False)
            socket_list.append(client_socket)
        
        for sockets in socket_list:
            try:
                recv_data = sockets.recv(1024).decode('utf-8')
            except Exception:
                pass
            else:
                if recv_data:
                    service_client(sockets, recv_data)
                else:
                    sockets.close()
                    socket_list.remove(sockets)

    tcp_socket.close()


if __name__ == "__main__":
    main()