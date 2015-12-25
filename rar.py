#!/usr/bin/env python
# encoding: utf-8


import os

for i in range(0, 100000):
    p = 'nsfocus'+(5-len(str(i)))*'0'+str(i)
    cmd = r"C:\Program Files (x86)\WinRAR\WinRar.exe e E:\\win.rar -y -p%s" % (p)

    r = os.system(cmd)
    if r == 1 or r == 0:
        print("pass = %s" % p)
        break

    print("%s %d" % (p, r))