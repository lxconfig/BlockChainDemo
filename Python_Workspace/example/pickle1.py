import pickle

load_file =  open("C:\\Users\\b\\Desktop\\新建文本文档.txt",'rb')
date = pickle.load(load_file)
print (date)
load_file.close()
