import socket
import re
import multiprocessing
import time
import mini_frame


class WSGIserver:
    def __init__(self):
        # 创建套接字
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 即使服务器被强制关闭，再次运行不会报错，地址可以再次使用
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定ip和port
        server_addr = ('', 53799)
        self.tcp_socket.bind(server_addr)

        # 将套接字由主动转为被动
        self.tcp_socket.listen(128)

    def service_client(self, client_socket):
        # 接收客户端发送的请求数据
            request_data = client_socket.recv(1024).decode("utf-8")
            # print(request_data)

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
            if not file_name.endswith('.py'):
                # 请求静态资源
                try:
                    with open("./html/"+file_name, "rb") as f:
                        file_content = f.read()
                except Exception as e:
                    print(e)
                    # 文件不存在返回404
                    response = 'HTTP/1.1 404 NOT FOUND\r\n'
                    response += "\r\n File Not Found!"
                    client_socket.send(response.encode("utf-8"))
                else:
                    # 根据请求数据返回页面
                    # windows中\r\n表示换行
                    response = 'HTTP/1.1 200 OK\r\n'
                    response += "\r\n"
                    # 返回两次，区分响应头和相应内容
                    client_socket.send(response.encode("utf-8"))
                    client_socket.send(file_content)
            else:
                # 请求动态资源
                # header = 'HTTP/1.1 200 OK\r\n\r\n'
                # body = "success %s" % time.ctime()
                # response = header + body
                # client_socket.send(response.encode('utf-8'))

                # 将判断返回何种资源的代码分离出去，达到解耦目的
                header = 'HTTP/1.1 200 OK\r\n\r\n'
                body = mini_frame.application(file_name)
                response = header + body
                client_socket.send(response.encode('utf-8'))
            
            # 关闭套接字
            client_socket.close()

    def run(self):
        while True:
            # 等待客户端的连接
            client_socket, _ = self.tcp_socket.accept()

            # 创建进程
            # 为客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(client_socket,))
            p.start()

            # 关闭为客户端服务的套接字
            # 进程会将代码再复制一份，所以还要再关闭一次client_socket
            client_socket.close()
            
        self.tcp_socket.close()


def main():
    """
        通过多进程和面向对象的方法，完成浏览器请求服务器的动态资源并返回
    """
    wsgi_server = WSGIserver()
    wsgi_server.run()


if __name__ == "__main__":
    main()