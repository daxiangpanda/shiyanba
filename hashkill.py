#!/usr/bin/env python
# encoding: utf-8

# Manhattan 曼哈顿
# Queens 皇后
# Brooklyn 布鲁克林
# The Bronx 布朗克斯
# Staten Island 斯塔滕岛

import hashlib
def check(src):
    m1 = hashlib.md5()
    m1.update(src)
    if m1.hexdigest() == '6ac66ed89ef9654cf25eb88c21f4ecd0':
        return True
    else:
        return False
newyork = ['Manhattan','Queens','Brooklyn','The Bronx','Staten Island']
# m1 = hashlib.md5()
def main():
    for i in range(1000):
        for j in newyork:
            for k in range(10000,15001):
                i = (3-len(str(i)))*'0'+str(i)
                # ctf{XXX_XXXXXXXXXXX_XXXXX}
                src = 'ctf{'+i+'_'+j.replace(' ','').lower()+'_'+str(k)+'}'
                if check(src):
                    return src
                else:
                    # print src
                    continue
# src = 'this is a md5'
# m1.update(src)
# print m1.hexdigest()

print main()