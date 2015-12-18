#!/usr/bin/env python
# encoding: utf-8

c = 'xztiofwhf'
for i in c:
    print chr((21*(ord(i)-ord('a')-11))%26+ord('a'))