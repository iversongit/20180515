import random
from flask import Blueprint, render_template, request, session, redirect, url_for,make_response

bp = Blueprint('app',__name__)

@bp.route('/login/',methods = ['GET','POST'])
def login():
    if request.method == "GET":
        username = session.get('username')
        return render_template('login.html',username=username)
    else:
        username = request.form.get('username')
        session['username'] = username
        return redirect(url_for('app.login'))

@bp.route('/getresponse/')
def get_response():
    ticket = ''
    response = make_response('<h2>haha</h2>')
    s = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for i in range(20):
        ticket += random.choice(s)
    # max_age -- 最大存活时间，以秒为单位 expire -- 过期时间
    response.set_cookie('ticket',ticket)
    return response,220

@bp.route('/deletecookie/')
def del_cookie():
    response = make_response('<h2>lalala</h2>')
    response.delete_cookie('ticket')
    return response