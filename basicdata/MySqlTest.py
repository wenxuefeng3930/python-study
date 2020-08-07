# mysql的连接和使用
import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.8.45",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database = "test"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

print(mydb)

mycursor.close()
