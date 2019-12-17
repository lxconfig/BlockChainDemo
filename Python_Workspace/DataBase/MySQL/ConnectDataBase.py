import pymysql


conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="lixuan",
        database="jing_dong",
        charset="utf8",
    )