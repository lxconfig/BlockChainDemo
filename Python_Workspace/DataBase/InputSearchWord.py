import pymysql


# def main():
#     content = str(input("请输入要查询的内容："))
#     conn = pymysql.connect(
#         host = "localhost",
#         port = 3306,
#         user = "root",
#         password = "lixuan",
#         database = "jing_dong",
#         charset = "utf8",
#     )
#     cursor = conn.cursor();
#     sql = "select " + content + " from goods;"
#     cursor.execute(sql)
#     print(cursor.fetchall())
class JD:
    def __init__(self):
        self.conn = pymysql.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "lixuan",
            database = "jing_dong",
            charset = "utf8",
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)  # 返回的是执行sql后查询出来的数量
        for item in self.cursor.fetchall():
            print(item)

    def show_all_items(self):
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_all_cates(self):
        sql = "select * from goods_cates;"
        self.execute_sql(sql)
        
    def show_all_brands(self):
        sql = "select * from goods_brands;"
        self.execute_sql(sql)
    
    @staticmethod
    def show_meun():
        print("------京东商品信息查询------")
        print("1. 查询所有商品")
        print("2. 查询所有的商品分类")
        print("3. 查询所有的品牌分类")
        print("4. 退出")
        return input("请输入查询的序号:")

    def run(self):
        while True:
            num = self.show_meun()  # JD.show_menu() or JD().show_menu()
            if num == "1":
                self.show_all_items()
            elif num == "2":
                self.show_all_cates()
            elif num == "3":
                self.show_all_brands()
            elif num == "4":
                print("感谢使用！")
                break 
            else:
                print("输入错误，请重新输入！")


def main():
    jd = JD()
    jd.run()

if __name__ == "__main__":
    main()