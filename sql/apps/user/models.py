# ORM  类--->表
# 类对象 ————> 表中的一条记录
from exts import db


# create table user(id int primarykey auto_increment, username varchar(20) not null,...)
class User(db.Model):
    # db.Column(类型，约束)映射表中的列 primary_key表示添加主键，autoincrement表示主键是自增
    """
    类型：
    db.Integer      int
    db.String(15)   varchar(15)
    db.Datetime     datetime_
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(20), unique=True)

    def __str__(self):
        return self.username
