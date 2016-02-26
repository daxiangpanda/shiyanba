#!/usr/bin/env python
# encoding: utf-8


import os

for i in range(0, 100000):
    p = (4-len(str(i)))*'0'+str(i)
    print p
    cmd = "C:\Program Files (x86)\7-Zip\7z.exe e E:\\ans.rar -y -p%s" % (p)

    r = os.system(cmd)
    if r == 1 or r == 0:
        print("pass = %s" % p)
        break

    print("%s %d" % (p, r))