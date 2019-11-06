#!/usr/bin/python
#-*-coding:utf-8 -*-
import csv
from Person import Person
from Combination import Combination
import sys

def read_csv():
    persons = []
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        raw_persons = list(reader)
    for p in raw_persons[1:]: # first line are the names
        # 调用了Person类中的__repr__方法
        # persons中保存的是Persons对象
        persons.append(Person('*', p[1], p[2], p[3], p[4]))
    return persons


def anonymize_sex(persons):#泛化性别
    for p in persons:
        p.sex = ''
    return persons         #返回列表型


def anonymize_ZIP(persons):#泛化邮编，一次泛化一位
    for p in persons:
        p.zipcode = p.zipcode[:-1]
    return persons         #返回列表型


def anonymize_date(persons):#泛化出生日期，一次泛化一位
    for p in persons:
        p.dob = p.dob[:-1]
    return persons          #返回列表型

def copy_persons(fresh_persons):#拷贝数据列表
    persons = []
    for p in fresh_persons:
        persons.append(Person(p.name, p.dob, p.sex, p.zipcode, p.illness))
    return persons


def group_persons(persons): #将数据分组，具体原理参考get_num
    grouped_persons = {}
    for p in persons:
        pseudo_parameters = str(p.dob) + str(p.zipcode) + str(p.sex)
        if grouped_persons.get(pseudo_parameters) is None:
            grouped_persons[pseudo_parameters] = []
        grouped_persons[pseudo_parameters].append(p)
    return grouped_persons  #返回字典型，每个组以键值对的形式存储


def get_k(grouped_persons):#获得k值（传入字典型泛化结果）
    tmpDict = {}
    for group in grouped_persons: #遍历所有键值对
        tmpDict[group] = len(grouped_persons[group])#获得每个键对应值的个数
                                              #即每个分组的包含的person个数
                             #以键(组标识)值(person个数)对存在字典tmpDict里
    k = None
    for group in tmpDict:     #遍历tmpDict，取出最小的person个数，赋值给k
        if k is None or tmpDict[group] < k:
            k = tmpDict[group]
    return k                #返回的k值即为泛化结果的k值


def export_csv(combination):
    print("结果导出中 ...")
    try:
        csv_list = [["姓名","出生日期","性别","邮编","所患疾病"]]
        for index, group in enumerate(combination.grouped_persons):
            for p in combination.grouped_persons[group]:
                csv_entry = str(p).split(', ')
                csv_list.append(csv_entry)
        with open("匿名化结果.csv", 'w') as myfile:
            wr = csv.writer(myfile, delimiter=",")
            wr.writerows(csv_list)
        print("结果导出成功!")
    except Exception as e:
        print("结果导出错误: " + str(e))

def get_num(persons,type):     #获得数据某属性个数（具体属性由type决定）
    get_num_ = {}              #一个字典（保存键值对）
    for p in persons:          #遍历数据
        if type==1:            #出生日期
            tmp_str = str(p.dob) #将某一个人的出生日期作为键tmp_str
        elif type==2:          #邮编
            tmp_str = str(p.zipcode)#将某一个人的邮编作为键tmp_str
        elif type==3:          #性别
            tmp_str = str(p.sex)#将某一个人的性别作为键tmp_str
        if get_num_.get(tmp_str) is None:#如果字典中没有此键
            get_num_[tmp_str] = [] #增加以tmp_str为键，值为空的键值对
        get_num_[tmp_str].append(p)#将此人的数据加到tmp_str键所对的值中
    tmp_str={}
    return len(get_num_)       #返回了字典中键的个数（就是属性个数）

def max_num(data_num,zip_num,sex_num):
    if data_num >= zip_num and data_num >= sex_num:
        return 1
    elif zip_num >= data_num and zip_num >= sex_num:
        return 2
    elif sex_num >= data_num and sex_num >= zip_num:
        return 3

def main():
    try:
        given_k = int(sys.argv[1])#你想要的k值
    except:
        print("输入您想要的K值  如: python anonymizer.py 4")
        exit()
    satisfying_combinations = []
    fresh_persons = read_csv()#从csv中读出数据,并泛化姓名

    persons = copy_persons(fresh_persons)
    while 1:
        grouped_persons = group_persons(persons) #将目前的数据分组
        k = get_k(grouped_persons) #得到目前的K值
        if k >= given_k:           #如果当前k值大于等于你得到的k值
            satisfying_combinations.append(Combination(k,grouped_persons))#将匿名结果添加到satisfying_combinations
            break                  #跳出循环
        data_num = get_num(persons,1)#出生日期属性个数 20
        zip_num = get_num(persons,2)#邮编属性个数 18
        sex_num = get_num(persons,3)#性别属性个数 2
        if data_num==1 and zip_num==1 and sex_num==1:
            break   #如果三个属性值都为1说明所有敏感属性全部泛化完成，跳出循环
        m = max_num(data_num,zip_num,sex_num)#返回属性个数最大的属性 20
        if m == 1:
            #如果是出生日期，对出生日期进行一位泛化
            anonymize_date(persons)
        elif m ==2:
            #如果是邮编，对邮编进行一位泛化
            anonymize_ZIP(persons)
        elif m ==3:
            #如果是sex，对sex泛化
            anonymize_sex(persons)
    if len(satisfying_combinations) > 0:#如果获得了数据的泛化结果
        print("实际K值为：" + str(k))    #输出k
        # print(persons)                   #输出泛化结果
        export_csv(Combination(k,grouped_persons))#导出到cvs
    else:                           #如果没得到，说明想要的k值大于可达到的最大k值
        print("K值设定过高. 请调整后再试!")

if __name__ == "__main__":
    main()

