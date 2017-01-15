# hello.py
# wsgi server : wsgiserver.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, Web!</h1>']

'''
    上面的 applicatio() 函数就是符合 WSGI 标准的一个 HTTP 处理函数，它接收两个参数：
        ·environ：一个包含所有 HTTP 请求信息的 dict 对象
        ·start_response：一个发送 HTTP 响应的函数
    
    在 application() 函数中，调用
        start_response('200 OK', [('Content-Type', 'text/html')])
    就发送了 HTTP 响应的 Header，但是只能发送一次，也就是这个函数只能调用一次。

    start_response() 函数接收两个参数，一个是 HTTP 响应码，一个是一组 list 表示的 HTTP Header，
    每个 Header 用一个包含两个 str 的 tuple 表示。

    通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。

    然后，函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。

    有了WSGI，我们关心的就是如何从 environ 这个 dict 对象拿到HTTP请求信息，然后构造 HTML，通过
    start_response() 发送 Header，最后返回 Body。

    最后，application() 函数必须由WSGI服务器来调用。
'''