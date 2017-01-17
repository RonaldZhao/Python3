#!E:\virtualenv\venv\Scripts\python.exe 
# -*- coding:utf-8 -*- 
''' 
题目：输入某年某月某日，判断这一天是这一年的第几天？注意校验输入的合法性。 
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊 
　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。 
2.程序源代码： 
''' 
def is_leap_year(year): 
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0): 
        return True 
    return False 
 
days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) 
 
while True: 
    year = int(input('Please input year:\n')) 
    month = int(input('Please input month:\n')) 
    day = int(input('Please input day:\n')) 
    sum = 0 
    error = False 
    if (month >= 1) and (month <= 12): 
        if month == 2: 
            if is_leap_year(year): 
                if day not in range(1, 30): 
                    error = True 
            else: 
                if day not in range(1, 29): 
                    error = True 
        else: 
            if day not in range(1, days_of_month[month-1]+1): 
                error = True 
        if error: 
            print('\nDay input Error!\n') 
            continue 
        for i in range(month - 1): 
            sum += days_of_month[i]
        sum += day
        if is_leap_year(year) and (month > 2): 
            sum += 1
        print('Today is the %dth day of the %d year.' % (sum, year)) 
        break 
    else: 
        print('\nMonth input Error!\n') 
        continue 