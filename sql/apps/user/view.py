from flask import Blueprint, url_for, request, render_template, redirect
from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def hello_world():
    return "Hi PaddleRS"

@user_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            # 与模型结合
            # 1.找到模型类并创建对象
            user = User()
            # 2.给对象赋值
            user.username = username
            user.password = password
            user.email = email
            # 添加
            # 3.将user对象添加到session中（类似缓存）
            db.session.add(user)
            # 4.提交数据
            db.session.commit()
            return render_template('user/result.html')
    return redirect('http://ylxb.natapp1.cc/register')

@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = User.query.filter_by(username=username)
        for user in users:
            if user.password == password:
                return redirect('http://ylxb.natapp1.cc/main')
        else:
            render_template('user/temp.html')
    return render_template('/user/temp.html')