import pymysql


def main():
    content = str(input("请输入要查询的内容："))
    conn = pymysql.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "lixuan",
        database = "jing_dong",
        charset = "utf8",
    )
    cursor = conn.cursor();
    sql = "select " + content + " from goods;"
    cursor.execute(sql)
    print(cursor.fetchall())



if __name__ == "__main__":
    main()