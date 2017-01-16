'''
    asyncio 是 Python 3.4 版本引入的标准库，直接内置了对异步 IO 支持。
   asyncio 的编程模型就是一个消息循环。我们从 asyncio 模型中直接获取一个 EventLoop 的引用，然后把需要执行的协程扔到
   EventLoop 中执行，就实现了异步 IO。
   用 asyncio 实现  Hello world 代码如下：
       e.g.1
   @asyncio.coroutine 把一个 generator 标记为 coroutine 类型，然后我们就把这个 coroutine 扔到 EventLoop 中执行。
   hello() 首先打印出 Hello world!，然后 yield from 语法可以让我们方便地调用另一个 generator。由于asyncio.sellp()
   也是一个 coroutine，所以线程不会等待 asyncio.sleep()，而是直接中断并执行下一个消息循环。当 asyncio.sleep()返回时，
   线程就可以从 yield from 拿到返回值(此处是None)，然后接着执行下一行的语句。
   把 asyncio.sleep(1) 看成是一个耗时 1 秒的 IO 操作，在此期间，主线程并未等待，而是去执行 EventLoop 中其他可以执行的
   coroutine 了，因此可以实现并发执行。
   下面用 tasks 封装两个 coroutine 试试：
       e.g.2
    观察执行过程：
        Hello world! (<_MainThread(MainThread, started 14092)>)
        Hello world! (<_MainThread(MainThread, started 14092)>)
        （间隔 1 秒）
        Hello again! (<_MainThread(MainThread, started 14092)>)
        Hello again! (<_MainThread(MainThread, started 14092)>)
    由打印的当前线程名称可以看出，两个 coroutine 是由同一个线程(MainThread)并发(started 14092)执行的。
    如果把 asyncio.sleep(1) 换成真正的 IO 操作，则多个 coroutine 就可以由一个线程并发执行。

    我们还可以用 asyncio 的异步网络来获取 sina、sohu、163的网站首页：
        e.g.3
    执行结果如下：
        暂时没网了，以后再添加...
    可见三个连接由一个线程通过 coroutine 并发完成。

    小结：
        asyncio 提供了完善的异步 IO 操作；
        异步操作需要在 coroutine 中通过 yield from 完成；
        多个 coroutine 可以通过封装成一组 tasks 然后并发完成。
'''
'''
e.g.1
# 用 asyncio 实现  Hello world 代码
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world!')
    # 异步调用 asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    # print(r)  # 此处 r == None
    print('Hello again!')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 执行 coroutine
    loop.run_until_complete(hello())
    loop.close()

'''
'''
e.g.2
import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

'''
'''
e.g.3

'''
import asyncio


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
