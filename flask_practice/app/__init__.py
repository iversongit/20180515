import os
from flask import Flask,Session
from flask_session import Session
from app.views import bp
import redis


def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(BASE_DIR,'templates')
    static_dir = os.path.join(BASE_DIR,'static')

    app = Flask(__name__,
                template_folder=templates_dir,
                static_folder=static_dir)
    app.register_blueprint(blueprint=bp,url_prefix='/app')
    # 127.0.0.1:8000/app/login/

    # 设置密钥
    app.config['SECRET_KEY'] = 'secret_key'
    # 使用redis存储信息
    app.config['SESSION_TYPE'] = 'redis'

    # 访问redis,不写下句则默认访问本地redis，即127.0.0.1:6379
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1',port='6379',password='')

    # 定义前缀
    app.config['SESSION_KEY_PREFIX'] = 'flask'

    # 初始化Session
    # 方式1
    Session(app)
    # 方式2
    # se = Session()
    # se.init_app(app)
    return app