# -*- coding:utf-8 -*-
import re


#  判断一个字符是否是汉字：是返回True，不是返回False
def is_chinese(s):
    return not isinstance(re.match(u'[\u4e00-\u9fff]+', s), type(None))

if __name__ == '__main__':

    characters = []  # 用来存储所出现的汉字
    stat = {}  # 用来存储每个汉字出现的次数
    total = 0  # 总字数

    with open('xyj.txt', 'r', encoding='utf-8') as fr:
        for line in fr:
            # 去掉一行两侧的空白
            line = line.strip()

            # 跳过空行
            if len(line) == 0:
                continue

            # 遍历该行的每一个字
            for s in line:
                # 如果是汉字
                if is_chinese(s):
                    total += 1
                    # 如果尚未记录在characters中
                    if s not in characters:
                        # 添加
                        characters.append(s)

                    # 如果尚未记录在stat中
                    if s not in stat.keys():
                        stat[s] = 0

                    # 汉字出现的次数 + 1
                    stat[s] += 1

    print('《西游记》一共用了 %d 个不同的汉字，共有 %d 个字。' % (len(characters), total))
    # print(len(stat))  # 应该等于 len(characters)才对

    # 用lambda 生成一个临时函数
    # d 表示字典的每一对键值，d[0]为key，d[1]为value
    # reversed为True表示降序排列
    stat = sorted(stat.items(), key=lambda d: d[1], reverse=True)

    # 定义一个文件，将统计结果和排序结果写入
    with open('result.csv', 'w') as fw:
        for item in stat:
            # 进行字符串拼接之前，需要将int转换为str
            fw.write(item[0] + ',' + str(item[1]) + '\n')
