file1 = []
count = 1
orign_file = open("C:\\Users\\b\\Desktop\\text.txt")
for each in orign_file:
    if each[:3] != "===":
        file1.append(each)
    else:
        file2 = 'C:\\Users\\b\\Desktop\\' + str(count) + ".txt"
        file3 = 'C:\\Users\\b\\Desktop\\' + str(count) + '.txt'
        log1 = open(file2,'w')
        log2 = open(file3,'w')
        log1.writelines(file1)
        log1.close()
        log2.close()

        file1 = []
        count += 1

file2 = 'C:\\Users\\b\\Desktop\\' + str(count) + ".txt"
file3 = 'C:\\Users\\b\\Desktop\\' + str(count) + '.txt'
log1 = open(file2,'w')
log2 = open(file3,'w')
log1.writelines(file1)
log1.close()
log2.close()

orign_file.close()
