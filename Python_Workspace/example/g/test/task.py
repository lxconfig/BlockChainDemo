def Create_file(text_1,text_2,count):
    file_1 = "C:\\Users\\b\\Desktop\\" + str(count) + ".txt"
    file_2 = "C:\\Users\\b\\Desktop\\" + str(count) + ".txt"

    dialogue_1 = open(file_1,'w')
    dialogue_2 = open(file_2,'w')

    dialogue_1.writelines(text_1)
    dialogue_2.writelines(text_2)

    dialogue_1.close()
    dialogue_2.close()



file = open("C:\\Users\\b\\Desktop\\text.txt")

text_1 = []
text_2 = []
count = 1

for each in file:
    if each[:7] != '=======':
        (role,talks) = each.split(":", 1)
        if role == '小甲鱼':
            text_1.append(talks)
        if role == '小客服':
            text_2.append(talks)
    else:
        Create_file(text_1,text_2,count)

        text_1 = []
        text_2 = []
        count += 1

Create_file(text_1,text_2,count)
file.close()
