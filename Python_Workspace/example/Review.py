import easygui as g
import os
import os.path

title = "请选择需要打开的文本文件"
h = g.fileopenbox(title = title)
with open(h) as f :
    q = f.read()
    t = g.textbox(title = "内" , text = q)

if t[:-1] != q :
    choice = g.buttonbox("文件变了，请选择以下操作：" , "警告" , ("覆盖保存" , "放弃保存" , "另存为"))
    if choice == "覆盖保存" :
        with open(h , 'w') as f :
            f.write(t[:-1])
    if choice == "放弃保存" :
        pass
    if choice == "另存为" :
        p = g.filesavebox(default = ".txt")
        with open(p , 'w') as f :
            f.write(t[:-1])
            
