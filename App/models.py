from App.ext import db


# 字母模型类
class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 字母
    name = db.Column(db.String(8))
    # 声明关系
    l_cities = db.relationship('City', backref='letter', lazy=True)

# 城市模型类
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 城市编号
    cityCode = db.Column(db.Integer)
    # 拼音
    pinYin = db.Column(db.String(40))
    # 中文名
    regionName = db.Column(db.String(40))
    # 声明关系(属于哪个字母下)
    c_letter = db.Column(db.Integer, db.ForeignKey(Letter.id))


# 用户模型类
class User(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    username = db.Column(db.String(80), unique=True)
    # 密码
    password = db.Column(db.String(256))
    # 邮箱
    email = db.Column(db.String(40), unique=True)
    # 手机
    phone = db.Column(db.String(20))

    # 等级
    permissions = db.Column(db.Integer, default=0)
    # 头像
    icon = db.Column(db.String(80), default='head.png')
    # 用户状态
    isactive = db.Column(db.Integer, default=0)
    # 令牌
    token = db.Column(db.String(256))
    # 逻辑删除
    isdelete = db.Column(db.Boolean, default=False)