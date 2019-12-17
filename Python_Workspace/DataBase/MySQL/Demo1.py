import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='lixuan',
    database="jing_dong",
    charset='utf8',
)

cursor = conn.cursor()

cursor.execute('select * from goods;')  # 返回查询的数量

line = cursor.fetchone()  # 输出一条查询的内容
print(line)
print(len(line))

for i in range(len(line)):
    print(line[i])

# print(cursor.fetchall())


# print(cursor.fetchmany(3))  # 输出指定数量的内容

cursor.close()
conn.close()
