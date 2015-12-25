#!/usr/bin/env python
# encoding: utf-8

c = 'aZZg/x\ZbavpZiEZp+n)o+'
c = c.lower()
print len(c)
for i in range(26):
    result = []
    for ii in c:
        if ord(ii) not in range(ord("A"),ord("Z")+1) and ord(ii) not in range(ord("a"),ord("z")+1):
            result.append(ii)
        else:
            result.append(chr((ord(ii)-ord("a")+i)%26+ord("a")))
    print ''.join(result)