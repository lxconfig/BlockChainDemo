from fdfs_client.client import Fdfs_client

client = Fdfs_client('/etc/fdfs/client.conf')
ret = client.upload_by_filename('/home/lixuan/图片/2019-10-28 15-34-53屏幕截图.png')

print(ret)