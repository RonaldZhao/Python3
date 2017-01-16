'''
    用 asyncio 提供的 @asyncio.coroutine 可以把一个 generator 标记为coroutine 类型，然后在 coroutine 内部
    用 yield from 调用另一个 coroutine 实现异步操作。 
    为了简化并更好地标识异步IO，从 Python 3.5 开始引入了新的语法 async 和 await，可以让 coroutine 的代码更简洁易读。 
    请注意，async 和 await 是针对 coroutine 的新语法，要使用新的语法，只需要做两步简单的替换： 
        1. 把 @asyncio.coroutine 替换为 async； 
        2. 把 yield from 替换为 await。 
    让我们对比一下 asyncio_Test.py 中的代码： 
        @asyncio.coroutine
        def hello():
            print("Hello world!")
            r = yield from asyncio.sleep(1)
            print("Hello again!")
    用新语法重新编写如下： 
    async def hello():
        print("Hello world!")
        r = await asyncio.sleep(1)
        print("Hello again!") 
    剩下的代码保持不变。 
    小结：
        Python 从 3.5 版本开始为 asyncio 提供了 async 和 await 的新语法； 
        注意新语法只能用在 Python 3.5 以及后续版本，如果使用 3.4 版本，则仍需使用上一节的方案。 
'''
# 将 asyncio_Test.py 的异步获取 sina、sohu 和 163 的网站首页源码用新语法重写并运行。 
import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
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
