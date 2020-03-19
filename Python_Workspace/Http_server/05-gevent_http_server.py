import socket
import re
import gevent
from gevent import monkey


monkey.patch_all()

def service_client(client_socket):
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
        
        # 关闭套接字
        client_socket.close()

def main():
    """
        通过多线程，完成浏览器请求服务器的资源并返回
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

    # while True:
    # 等待客户端的连接
    client_socket, _ = tcp_socket.accept()

    # 创建进程
    # 为客户端服务
    p = gevent.spawn(service_client, client_socket)
    p.join()

    # 关闭为客户端服务的套接字
    # 进程会将代码再复制一份，所以还要再关闭一次client_socket
    # 线程则不需要,协程也不需要
    # client_socket.close()
        
    tcp_socket.close()


if __name__ == "__main__":
    main()