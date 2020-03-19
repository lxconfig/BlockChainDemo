import cv2
import  os
import collections
 
readPath=r"./save"
files=os.listdir(readPath)
n=0
s=''
for file in files  :
    li=[]
    n+=1
    imgPath = readPath + "\\" + file
    img=cv2.imread(imgPath)
    for i in range(100):
        for j in range(100):
            b=img[i,j,0]
            g=img[i,j,1]
            r=img[i,j,2]
            li.append((b,g,r))
 
    most=collections.Counter(li).most_common(1)
    s += file
    s += ":"
    s += str(most[0][0]).replace("(","").replace(")","")
    s += "\n"
    print(n)
 
f = open('filename.txt','w')
f.write(s)