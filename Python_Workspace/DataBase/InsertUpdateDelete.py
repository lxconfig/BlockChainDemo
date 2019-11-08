import pymysql
import ConnectDataBase


def main():
    cursor = ConnectDataBase.conn.cursor();
    # Insert_sql = "insert into goods_cates (name) values ('机械革命');"
    # Update_sql = "update goods_cates set name='机械革命x' where name='机械革命';"
    # delete_sql = "delete from goods_cates where id=8;"
    # cursor.execute(Insert_sql)  # 执行sql后，为了安全，不会直接在数据库中增加一条数据
    # cursor.execute(Update_sql)
    # conn.commit()  # 只有在commit之后，之前对数据库的所有改动才会真正生效(包括插入、修改、删除)
    # conn.rollback()  # 撤销之前所有的sql执行结果


    name = input("输入:")
    # sql = "select * from goods where name ='%s'" % name;  # 存在sql注入的情况
    sql = "select * from goods where name = %s"
    print("----->%s<------" % sql)
    cursor.execute(sql, [name])  # 让execute自己拼装sql语句执行，可以防止sql注入
    print(cursor.fetchall())
    # for item in cursor.fetchall():
    #     print(item)


if __name__ == "__main__":
    main()