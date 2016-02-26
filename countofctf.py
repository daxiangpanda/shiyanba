#!/usr/bin/env python
# encoding: utf-8

with open(r'E:\dictionary.txt','r') as f:
    n = f.read()
words = n.split('\n')
# print words[0]
num = 0
for i in words:
    if 'ctf' in i:
        num+=len(i)
        print i
print len(words)
print num