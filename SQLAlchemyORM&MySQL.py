# 用SQLAlchemy ORM在MySQL的test数据库中创建的user表

# 1.导入SQLAlchemy，并初始化DBSession：
# 导入：
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接(创建数据库引擎)：
# create_engine()用来初始化数据库连接。
# SQLAlchemy用一个字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:Tux_970212**-..@localhost:3306/test')
# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)
# 创建数据表基类：
Base = declarative_base()

# 定义User对象(表)：
class User(Base):
    # 表的名字：
    __tablename__ = 'user'

    # 表的结构：
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return "<User(id='%s', name='%s')>" % (self.id, self.name)

# 定义City对象(表)：
class City(Base):
    __tablename__ = 'city'
    num = Column(String(10), primary_key=True)
    name = Column(String(50))

# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class。

# 创建数据表：
Base.metadata.create_all(engine)

# 增删查改的前提，先创建session对象：
session = DBSession()

'''
    增：
    下面展示如何向数据库 添加 一行记录：
    由于有了ORM，我们向数据库添加一行记录，可以视为添加一个User对象：
'''

# 创建新User对象：
new_user = User(id='0', name='zt')
cities = [
    City(num='010', name='Beijing'),
    City(num='0311', name='Shijiazhuang'),
    City(num='0791', name='Nanchang')]
# 创建新City对象：
new_city = City(num='0318', name='Hengshui')
# 添加到session：
try:
    session.add(new_user)
    session.add(new_city)
    session.add_all(cities)
    # 提交即保存到数据库：
    session.commit()
except:
    # 添加发生错误时回滚
    session.rollback()

'''
    可见，关键是获取session，然后把对象添加到session，最后提交并关闭。
    DBSession对象可视为当前数据库连接。
'''

'''
    查：
    如何从数据库表中 查询 数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。
    SQLAlchemy提供的查询接口如下：
'''
# 创建Query查询， filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行。
user = session.query(User).filter(User.id=='0').one()
cities = session.query(City).all()
# 打印：
print('type:', type(user), user.id, user.name)
for row in cities:
    print(row.num, row.name)

'''
    改：
'''
try:
    upuser = session.query(User).filter(User.id=='0').one()
    upuser.name = 'ztuptozzg'
    session.commit()
except:
    session.rollback()
'''
    删：
'''
try:
    session.delete(session.query(City).filter(City.num=='0791').one())
    session.commit()
    # print(session.query(User).filter(City.num=='0791').count())
except:
    session.rollback()

# 操作完毕后要关闭session：
session.close()
