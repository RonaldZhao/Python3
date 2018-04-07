Python2.x和Python3.x的区别

1. Python3.x 不向下(低于Python2.x)兼容；



下面使用一个表格来对比其不同(来源于[runoob](http://www.runoob.com/python/python-2x-3x.html))：

|          对比内容          |                          Python2.x                           |                          Python3.x                           |
| :------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|       print,print()        |                       print是一个语句                        |                      print()是一个函数                       |
|          Unicode           | Python 2 有 ASCII str() 类型，unicode() 是单独的，不是 byte 类型。 | 在 Python 3，我们有 Unicode (utf-8) 字符串，以及一个字节类：byte 和 bytearrays。而且 Python3.x 源码文件默认使用utf-8编码 |
| 除法运算('//'运算没有改变) | Python 2中 **/** 运算两个整数相除的结果是一个整数，完全忽略小数部分；浮点数相除才会保留小数点部分 |  Python 3中的 **/** 运算即使是两个整数相除也会保留小数部分   |
|            异常            |             捕获异常的语法为 **except exc, var**             | 使用 **as** 作为关键词， 改为 **except exc as var**，而且使用语法**except (exc1, exc2) as var**可以同时捕获多种类别的异常 |
|            异常            |              所有类型的对象都是可以被直接抛出的              |        只有继承自**BaseException**的对象才可以被抛出         |
|            异常            |        **raise**语句使用逗号将抛出对象类型和参数分开         |               改为直接调用构造函数抛出对象即可               |
|           xrange           |                       用来创建迭代对象                       |                       更名为**range**                        |
|      八进制字面量表示      |            例如512的八进制：512=01000或512=0o1000            |           只能用512=0o1000，而01000的写法取消使用            |
|         不等运算符         |                    有两种：**!=**，**<>**                    |                         只能用**!=**                         |
|     去掉了repr表达式``     |        Python 2.x 中反引号**``**相当于repr函数的作用         |    Python 3.x 中去掉了**``这种**写法，只允许使用repr函数     |
|  多个模块被改名(根据PEP8)  | _winreg、 ConfigParser、copy_reg、Queue、SocketServer、repr  | 改为：winreg、configparser、copyreg、queue、socketserver、reprlib |
|          数据类型          |                                                              | 去除了**long**类型，**int**类型的行为就像Python2.x中的**long**；新增**bytes**类型，对应Python2.x中的八位串，定义一个bytes字面量的方法为：**b = b'python'**； **str**对象和**bytes**对象可以使用.encode() (str -> bytes) or .decode() (bytes -> str)方法相互转化。 |

其他详细信息请参见官方文档或待我慢慢整理，感谢参考。