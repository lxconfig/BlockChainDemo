# -*- coding:utf-8 -*-
# time: 2019/03/14 19:02
# File: 9-pytesseract.py
import datetime
import pytesseract
from PIL import Image
from PIL import ImageEnhance

start = datetime.datetime.now()
# 打开图片
img = Image.open('code.png')
enhancer = ImageEnhance.Color(img)
enhancer = enhancer.enhance(0)
enhancer = ImageEnhance.Brightness(enhancer)
enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
img = enhancer.enhance(20)
# 转化为灰度图片
img = img.convert('L')
# 显示图片
# img.show()
# 二值化处理
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = img.point(table, '1')
# out.show()
img = img.convert('RGB')
# 识别图片
print(pytesseract.image_to_string(img))


end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")