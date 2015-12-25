# -*- coding: utf-8 -*-
__author__ = '31351'

import itertools
output = []
for i in list(itertools.permutations([1,2,3,4,5,6,7,8,9,10],10)):
    a,b,c,d,e,f,g,h,i,j = i
    if g+b+a == f+a+e and f+a+e == j+e+d and j+e+d == i+d+h and i+d+h == h+c+b:
        mini = min(f,g,h,i,j)
        print mini
        n1 = str(f)+str(a)+str(e)
        n2 = str(g)+str(b)+str(a)
        n3 = str(h)+str(c)+str(b)
        n4 = str(i)+str(d)+str(c)
        n5 = str(j)+str(e)+str(d)
        print n1
        print n2
        print n3
        print n4
        print n5
        if mini == f:
            result = n1+n5+n4+n3+n2
        elif mini == g:
            result = n2+n1+n5+n4+n3
        elif mini == h:
            result = n3+n2+n1+n5+n4
        elif mini == i:
            result = n4+n3+n2+n1+n5
        elif mini == j:
            result = n5+n4+n3+n2+n1
        print result
        # print len(result)
        if len(result) == 16:
            # print type(result)
            output.append(int(result))
print max(output)
# http://ctf1.shiyanbar.com/program/2/
# 答案是5728249411013637
# print n1,n2,n3,n4,n5

        # print a,b,c,d,e,f,g,h,i,j