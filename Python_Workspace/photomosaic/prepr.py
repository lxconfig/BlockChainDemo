import os#和文件有关的模块
import cv2#OpenCV
 
#这里是10万张图片所在的文件夹，你可以按照你的路径改下面的代码。另外路径好像不支持中文字符。
readPath=r"./photo"

#这里是改变大小之后的图片，要保存的路径。save是一个文件夹
savePath=r"./save"
 
#用一个列表保存所有的图片的文件名字
files=os.listdir(readPath)
 
#n变量用来看到10万张图片的处理进度。
n=0
 
#遍历所有图片文件们
for file in files:
    n+=1
    imgPath=readPath+ "\\" + file#构造图片路径
    img=cv2.imread(imgPath)#读取图片到内存img变量
    img=cv2.resize(img,(100,100))#更改图片的大小
    # 更改之后写入文件，方便以后使用。否则你生成一张马赛克就要处理一次10万张图片
    cv2.imwrite(savePath+ "\\"+file,img)
    print(n)

# savePath = r"E:\python_file\code\photomosaic"

# imgPath="./zbq.jpg"#构造图片路径
# img=cv2.imread(imgPath)#读取图片到内存img变量
# img=cv2.resize(img,(300,300))#更改图片的大小
# # 更改之后写入文件，方便以后使用。否则你生成一张马赛克就要处理一次10万张图片
# cv2.imwrite(savePath+ "\\"+"zbq2.jpg",img)
# print(n)
    
cv2.waitKey()