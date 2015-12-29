#! /usr/bin/python
# 014_1.py
import math
number = 24735874714315080754352345095703661322548673352435942903195989882233787254754

list = []

def getChildren(num):
    print '*'*30
    isZhishu = True
    i = 2
    square = int(math.sqrt(num)) + 1
    while i <= square:
        # print i
        if num % i == 0:
            list.append(i)
            isZhishu = False
            getChildren(num / i)
            i += 1
            break
        i += 1
    if isZhishu:
        list.append(num)

getChildren(number)
print list