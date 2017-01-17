#!E:\virtualenv\venv\Scripts\python.exe
# -*- coding:utf-8 -*-
'''
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
1.程序分析：我们首先初始化一个空的list，然后通过一个for循环来接收输入的整数，每次接收后转换为整数并存放在x中，
            然后把x添加到list中，最后把list使用sort()函数排序即可。
2.程序源代码：
'''
l = []
for i in range(3):
    x = int(input('Please input number: '))
    l.append(x)
l.sort()
print('Sorted numbers:',l)
