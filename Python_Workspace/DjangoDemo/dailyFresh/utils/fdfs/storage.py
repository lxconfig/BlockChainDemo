'''
@Author: lixuan
@Date: 2020-01-08 16:57:48
@LastEditTime : 2020-01-09 11:20:10
@Description: 自定义文件存储类
'''
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings

class FdfsStorage(Storage):
    """fastDFS文件存储类"""
    def __init__(self, client_conf_path=None, fdfs_nginx_url=None):
        if client_conf_path is None:
            client_conf_path = settings.FDFS_CLIENT_CONF_PATH
        self.client_conf_path = client_conf_path

        if fdfs_nginx_url is None:
            fdfs_nginx_url = settings.FDFS_NGINX_URL
        self.fdfs_nginx_url = fdfs_nginx_url

    def _open(self, name, mode='rb'):
        """打开文件时调用"""
        pass

    def _save(self, name, content):
        """保存文件时调用"""
        # name: 上传文件的名字
        # content: 包含上传文件内容的File对象

        # 创建一个Fdfs_client对象
        client = Fdfs_client(self.client_conf_path)
        # 上传文件到FastDfs系统中
        # 通过文件内容上传
        res = client.upload_by_buffer(content.read())

        if res.get("Status") != "Upload successed.":
            raise Exception("上传文件到FastDFS失败")
            
        # 返回文件的ID
        return res.get('Remote file_id')
    
    def exists(self, name):
        """判断文件名是否可用"""
        # 返回True表示文件名已存在
        # 返回False表示文件名不存在
        return False
    
    def url(self, name):
        """返回上传文件的url路径"""
        return self.fdfs_nginx_url + name