#!/usr/bin/env python
# encoding: utf-8

import os
dir="E:\\shiyanba\\安全杂项\\你有记日志的习惯吗\\www\\"
for root,dirs,files in os.walk(dir):
    for file in files:
        with open(os.path.join(root,file),'r') as f:
            n = f.read()
            print n
            if 'key' or 'KEY' in n:
                print os.path.join(root,file)