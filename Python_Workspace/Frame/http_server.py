import socket
import threading
import re
# import frame.frame  as frame  # 导入框架
import sys


class WSGIserver:
    def __init__(self, port, app, static_path):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = ('', port)
        self.tcp_socket.bind(server_addr)
        self.tcp_socket.listen(128)
        self.app = app
        self.static_path = static_path
    
    def static_file(self, file_name):
        '''
            返回静态文件
        '''
        try:
            with open(self.static_path+file_name, 'r', encoding="utf-8") as f:
                content = f.read()
        except Exception:
            headers = 'HTTP/1.1 404 NOT FOUND\r\n'
            body = '\r\n FILE NOT FOUND'
            response = headers + body
        else:
            headers = 'HTTP/1.1 200 OK\r\n'
            body = "\r\n" + content
            response = headers + body
        return response


    def service_client(self, client_socket):
        '''
            为客户端服务
        '''
        request_data = client_socket.recv(1024).decode("utf-8")
        # print(request_data)
        request = str(request_data).splitlines()
        # Get /index.html HTTP/1.1
        # r"[^/]+/([^ ]*)"
        ret = re.match(r'[^/]+/([^ ]*)', request[0])
        if ret:
            file_name = ret.group(1)
        else:
            file_name = "index.html"
        # 判断请求的是静态资源还是动态
        if file_name.endswith('.py'):
            # 动态资源，借助框架进行处理
            environ = dict()
            environ['file_name'] = file_name
            environ['static_path'] = self.static_path
            body = self.app(environ, self.set_response)
            headers = 'HTTP/1.1 %s\r\n' % self.status
            for i in self.headers:
                headers += "%s:%s\r\n\r\n" % (i[0],i[1])
            response = headers + body
        else:
            # 静态资源
            response = self.static_file(file_name)
        client_socket.send(response.encode('utf-8'))


    def set_response(self, status, headers):
        '''接收application()函数设置的响应头'''
        self.status = status
        self.headers = headers

    
    def run(self):
        # while True:
        client_socket, _ = self.tcp_socket.accept()  # 等待连接

        thread = threading.Thread(target=self.service_client, args=(client_socket, ))  # 为客户端服务
        thread.start()
        # service_client(client_socket)

        self.tcp_socket.close()  # 关闭套接字


def main():
    """
        http服务器
    """
    # 通过命令启动时，按以下格式: python xxx.py 8899 frame:application
    parameters = sys.argv
    if len(parameters) == 3:
        try:
            port = int(parameters[1])
            frame_app = parameters[2]
        except Exception:
            print("请按以下格式运行: python xxx.py 8899 frame:application")
            return
    else:
        print("请按以下格式运行: python xxx.py 8899 frame:application")
        return

    ret = re.match(r'([^:]+):(.*)', frame_app)
    if ret:
        frame_name = ret.group(1)
        frame_func = ret.group(2)
    else:
        print("请按以下格式运行: python xxx.py 8899 frame:application")
        return
    
    sys.path.append('./frame')
    # 导入框架
    frame = __import__(frame_name)
    app = getattr(frame, frame_func)

    # 读取配置文件
    with open('./conf/web_server.conf', 'r') as f:
        conf_info = eval(f.read())

    server = WSGIserver(port, app, conf_info['STATIC_PATH'])
    server.run()

if __name__ == "__main__":
    main()