'''
    使用 Flask 处理 3 个URL，分别是：
    ·GET /：首页，返回 Home；
    ·GET /signin：登录页，显示登录表单；
    ·POST /signin：处理登录表单，显示登录结果。
    注意：同一个 URL/signin 分别有 GET 和 POST 两种请求，映射到两个处理函数中。
'''

'''
    （测试环境：Python 3.6.0）
    在终端运行 app.py ，Flask 自带的 Server 将在端口 5000 上监听：
    $ python app.py
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    打开浏览器，输入首页地址 http://127.0.0.1:5000/ ，将返回 首页的 'Home'；
    再在浏览器地址栏输入 http://127.0.0.1:5000/signin ，会显示登录表单；
    输入预设的用户名 admin 和口令 password ，登陆成功，显示 'Hello, admin'，
    输入其他错误的用户名和口令将显示 'Bad username or password'；
'''
# Flask 通过 Python 的装饰器在内部自动地把 URL 和函数关联起来。
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从 request 对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()