# 主要用来处理业务逻辑
import uuid
from flask import render_template, request, make_response, redirect, abort
from flask import Blueprint,url_for

bp = Blueprint('first',__name__)  # 初始化Blueprint -- 管理、规划url, first -- 创建的蓝图名称
# print("Blueprint...",__name__)  # __name__ == app.views 即当前所在的模块

@bp.route('/',methods=['GET','POST']) # 指定路由地址，默认(127.0.0.1:5000) methods:指定请求方式
def hi(): # 视图函数
    return 'hi,how are you?'

@bp.route('/hello/<name>') # name: str类型，可以接收各种类型的参数
def hello_man(name):
    print(name)  #  -- name
    print(type(name)) # -- 'str'
    return 'hello %s' % name

@bp.route('/helloint/<int:id>/') # 指定了参数类型，只能接收int类型的参数
def hello_int(id):
    print(id) # -- id
    print(type(id)) # -- 'int'
    # a = "yusir"
    # 1/0
    return 'hello int: %s' %(id)

@bp.route('/index/')
def indexing():
    # 返回指定页面 如果不加../  则会找本级目录下的templates
    # return send_file("../templates/hello.html")
    return render_template("hello.html")

@bp.route('/getfloat/<float:price>/')
def hellofloat(price):
    return 'float: %s' % price

@bp.route('/getname/<string:name>/')
def helloname(name):
    return 'name: %s' % name

@bp.route('/getpath/<path:url_path>/')
# 紧挨着路由的视图函数将被调用，且其形参名必须
# 与url中的变量名保持一致
def hellopath(url_path):
    return 'path path path!! -- %s' % url_path

@bp.route('/getuuid/')
def getuuid():
    a = uuid.uuid4()
    # print("uuid",type(a))
    return str(a)  # uuid类型的数据不能被直接打印，需要转换成string类型再打印

@bp.route('/getbyuuid/<uuid:uu>/')  # 如果不能输入正确格式的uuid数据，将会报错
def hellouuid(uu):
    return 'uu:%s' % uu

@bp.route('/getrequest/',methods=['GET','POST'])
# ImmutableMultiDict格式的字典，
# 这种格式的数据时不可变的，这时在使用.to_dict()
# 就可以转换成常规字典类型了
def get_request():
    if request.method == "GET":
        args = request.args
    if request.method == "POST":
        form = request.form
    return '获取request'

@bp.route('/makeresponse/')
def make_resposes():
    temp = render_template("hello.html")
    # response = make_response('<h2>哈哈</h2>')
    # 250 -- 请求响应状态码 与在return中写状态码效果一样
    response = make_response(temp,250)
    # response = make_response(temp)
    # return response, 250
    return response

@bp.route('/redirect/') # 跳转方法
def make_redirect():
    # 第一种方法
    # return redirect('hello/index/')
    # 第二种方法
    return redirect(url_for('first.indexing'))  # first:蓝图名 indexing:蓝图下的方法 indexing已经和地址绑定在一起

@bp.route('/makeabort/')
def make_abort():
    abort(404) # 抛出404异常
    return '终结'

@bp.errorhandler(404)  # 捕捉指定异常
def get_error(exception):
    return '捕捉异常: %s' % exception