'''
text_file=open('C:\\Users\\b\\Desktop\\08-08.log')
text=text_file.read()
print(text)
'''

'''
test_file = open("C:\\Users\\b\\Desktop\\08-08.log",'w')
test_file.write("this is my test file")
test_file.close()

test_file = open("C:\\Users\\b\\Desktop\\08-08.log")
test=test_file.read()
print(test)

'''


'''
a = abs(10)+abs(-10)
print (a)
b = abs(-10)+ -10
print (b)

'''

file = open("C:\\Users\\b\\Desktop\\08-08.log")
text = file.read()
#print(text)
file.close()

file = open("C:\\Users\\b\\Desktop\\tet.txt",'w')
file.write(text)
file.close()
