# MySQL数据库连接及操作(py3.6下测试通过)

# 1.导入MySQL驱动(mysql-connector)
import mysql.connector

# 2.连接到需要操作的数据库
conn = mysql.connector.connect(user='root', password='Tux_970212**-..', database='test')

# 3.获取数据库游标
cur = conn.cursor()

# 4.相关操作

# 创建user表
sql = 'drop table if exists user'
cur.execute(sql)
sql = 'create table user(id varchar(20) primary key not null, name varchar(20) not null)'  # 定义SQL语句
cur.execute(sql)  # 执行SQL语句
print(cur.rowcount)  # 输出受影响的行数

# 插入两行记录，注意MySQL的占位符是%s
sql = 'insert into user (id, name) values (%s, %s)'
cur.execute(sql, ['1', 'gitzzg'])
print(cur.rowcount)
cur.execute(sql, ['2', 'zzglovezt'])
print(cur.rowcount)

# 提交事务，这样所做的操作才能真正更改数据库
conn.commit()

# 查询数据库中的记录
sql = 'select * from user'
cur.execute(sql)
# 查询完毕将返回一个结果集，所以需要用fetchall()函数将其中的所有数据取出
data = cur.fetchall()
for v in data:
    print(v)

# 操作完毕后先关闭游标
cur.close()
# 再关闭数据库连接
conn.close()
