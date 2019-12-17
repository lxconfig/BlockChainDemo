'''
@Author: lixuan
@Date: 2019-11-13 16:52:08
@LastEditTime: 2019-11-13 16:57:12
@Description: 数据库索引功能测试
'''
import ConnectDataBase


def main():
    cursor = ConnectDataBase.conn.cursor();
    for i in range(1000):
        cursor.execute("insert into test_index values('ha-%d')" % i)
    
    ConnectDataBase.conn.commit()




if __name__ == "__main__":
    main()