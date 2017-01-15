from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin_ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()

'''
    什么是 MVC？
        MVC 是什么？ MVC = Model-View-Controller，中文名"模型-视图-控制器"。
    为什么要用 MVC？
        Web APP 最复杂的部分就在 HTML 页面。HTML 不仅要正确，还要通过 CSS 美化，再加上复杂的 JavaScript 脚本
        来实现各种交互和动画效果。总之，生成 HTML 页面的难度很大。
        又由于在 Python 代码里拼接字符串是不现实的，所以，就有了模板技术。
    MVC 原理：
        使用模板，我们需要预先准备一个 HTML 文档，这个 HTML 文档不是普通的 HTML，而是嵌入了一些变量和指令，然后
        根据我们传入的数据，替换后，得到最终的 HTML，发送给用户：
            浏览器请求：GET /gitzzg   ------->
                                            |
                                            |   name = 'gitzzg'
                                      -------
                                     \|/
               app.py：@app.route('/<name>')
                       def home(name):
                           return render_template('home.html', name=name)
                                                              |
                                           --------------------
                 模板: <html>              |  变量 {{ name }} 替换为"gitzzg"
                       <body>             \|/
                            <p>Hello, {{ name }}!</p>
                       </body>
                       </html>
                          |
                          | 输出
                         \|/
           用户看到的：<html>
                      <body>
                            <p>Hello, Michael!</p>
                      </body>
                      </html>
        Python 处理 URL 的函数就是 C：Controller，Controller 负责业务逻辑，比如检查用户名是否存在，取出用户信息等等。
        包含变量 {{ name }} 的模板就是 V：View，View 负责显示逻辑，通过简单的替换一些变量，View 最终输出的就是用户看到
        的 HTML。
        MVC 中的 Model 是用来传给 View 的，这样 View 在替换变量的时候，就可以从 Model 中取出相应的数据。
        上面的例子中，Model 就是一个 dict：
        {'name': 'gitzzg'}
        只是因为 Python 支持关键字参数，很多 Web 框架允许传入关键字参数，然后，在框架内部组装出一个 dict 作为 Model。
    上面的代码是把 app.py 中直接输出字符串作为 HTML 的例子用 MVC 模式改写一下：
        切记一定要把模板放在正确的 templates 目录下，templates 和 此文件在同一目录。
'''

'''
    Flask 通过 render_template() 函数来实现模板的渲染。
    和 Web 框架类似，Python 模板也有很多种。
    Flask 默认支持的模板是 jinja2，所以安装好 jinja2 后就可以开始写 jinja2 模板了。
'''