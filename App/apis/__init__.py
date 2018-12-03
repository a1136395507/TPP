from flask_restful import Api

from App.apis.ActiveApi import UserActive
from App.apis.CityApi import CityResource
from App.apis.HelloApi import Hello
from App.apis.IconApi import UserIcon
from App.apis.LoginApi import Login
from App.apis.PasswordApi import Password
from App.apis.RegisterApi import Register

api = Api()

def init_api(app):
    api.init_app(app)


# 添加资源
api.add_resource(Hello, '/hello/')

api.add_resource(CityResource, '/api/v1/citylist/') # 城市列表
api.add_resource(Register, '/api/v1/register/') # 注册
api.add_resource(UserActive, '/api/v1/active/') # 用户激活
api.add_resource(Login, '/api/v1/login/')   # 登录
api.add_resource(Password, '/api/v1/updatepd/') # 修改密码
api.add_resource(UserIcon, '/api/v1/usericon/') # 用户头像