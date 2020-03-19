import os#和文件有关的模块
import cv2#OpenCV
 
 
#n变量用来看到10万张图片的处理进度。
n=0


savePath = r"E:\python_file\code\photomosaic"

imgPath="./zbq.jpg"#构造图片路径
img=cv2.imread(imgPath)#读取图片到内存img变量
img=cv2.resize(img,(300,300))#更改图片的大小
# 更改之后写入文件，方便以后使用。否则你生成一张马赛克就要处理一次10万张图片
cv2.imwrite(savePath+ "\\"+"zbq2.jpg",img)
print(n)
    
cv2.waitKey()