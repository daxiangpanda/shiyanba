#!/usr/bin/env python
# encoding: utf-8

import os
# print os.getcwd()
f = open(os.path.join(os.getcwd()+'\\new'),'wb')
# f.write('ss')
# f.write('bbb')
for file in os.listdir(os.getcwd()+'\\onlyOneFile'):
    with open(os.path.join(os.getcwd()+'\\onlyOneFile',file),'rb') as g:
        # print g.read()
        f.write(g.read())
f.close()