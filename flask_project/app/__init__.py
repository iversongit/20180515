import os

from flask import Flask
from app.views import bp

def create_app():
    # __file__ -- F:\\Python\\PythonCode\\20180515\\flask_project2\\app\\__init__.py
    # os.path.abspath(__file__) --
    #      F:\\Python\\PythonCode\\20180515\\flask_project2\\app\\__init__.py
    # os.path.dirname(os.path.abspath(__file__)) --
    #      F:\\Python\\PythonCode\\20180515\\flask_project2\\app
    # os.path.dirname(os.path.dirname(os.path.abspath(__file__))) --
    #      F:\\Python\\PythonCode\\20180515\\flask_project2
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # templates_dir -- F:\\Python\\PythonCode\\20180515\\flask_project2\\templates
    templates_dir = os.path.join(BASE_DIR,'templates')
    # static_dir -- F:\\Python\\PythonCode\\20180515\\flask_project2\\static_dir
    static_dir = os.path.join(BASE_DIR,'static')

    # 初始化  __name__：主模块名或者包
    # template_folder=templates_dir -- 绑定templates文件夹路径
    # static_folder=static_dir -- 绑定static文件夹路径
    app = Flask(__name__,template_folder=templates_dir,static_folder=static_dir)  # app: flask对象
    # print("init...",__name__) # __name__ == app 即包名

    # 绑定蓝图对象，操纵指定模块中的url
    # 为了区分不同的蓝图，使用url_prefix指定前缀，访问时需先加前缀再加访问地址
    app.register_blueprint(blueprint=bp,url_prefix='/hello/')
    return app