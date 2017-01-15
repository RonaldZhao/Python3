'''
    Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。
    所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
'''

# 从 wsgiref 模块导入
from wsgiref.simple_server import make_server
# 导入自己编写的 application() 函数
from hello import application

# 创建一个服务器，IP 地址为空，端口是 8000，处理函数是 application()
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听 HTTP 请求：
httpd.serve_forever()

'''
    首先在终端运行此文件，然后在浏览器输入 localhost:8000 即可
'''