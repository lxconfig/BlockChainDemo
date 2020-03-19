import  cv2
import numpy as np
 
readPath=r"./save"
 
def readIndex():
    fs = open("filename.txt","r")
    n=0
    dic=[]
    for line in fs.readlines():
        n+=1
        temp=line.split(":")
        file=temp[0]
        bgr=temp[1].split(",")
        b=int(bgr[0])
        g=int(bgr[1])
        r=int(bgr[2])
        dic.append((file,(b,g,r)))
    return dic
 
 
img=cv2.imread("zbq2.jpg")
s=np.shape(img)
print(s)
big= np.zeros((100*s[0], 100*s[1], 3), dtype=np.uint8)
 
list=readIndex()#读取索引文件到变量中
 
for i in range(s[0]):#遍历行和列
    for j in range(s[1]):
        print(i)
        b = img[i, j, 0]
        g = img[i, j, 1]
        r = img[i, j, 2]#获取图像当前位置的BGR值
        
        np.random.shuffle(list)#打乱索引文件
        
        for item in list:
            imgb=item[1][0]
            imgg=item[1][1]
            imgr=item[1][2]#获取索引文件的RGB值
            
            distance=(imgb-b)**2+(imgg-g)**2+(imgr-r)**2#欧式距离
            if distance<100:
                filepath=readPath+"\\"+str(item[0])#定位到具体的图片文件
                break
        little=cv2.imread(filepath)#读取整个最相近的图片
        big[i*100:(i+1)*100,j*100:(j+1)*100]=little#把图片画到大图的相应位置
 
cv2.imwrite("bigzbq.jpg",big)#输出大图到文件中