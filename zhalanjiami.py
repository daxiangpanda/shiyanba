#!/usr/bin/env python
# encoding: utf-8

c = 'kyssmlxeei{ipeu}'
odd = []
even = []
for i in range(len(c)):

    if i%2 == 0:
        odd.append(c[i])
    else:
        even.append(c[i])
zhalan='puysleiie'

for i in range(26):
    result = []
    for ii in zhalan:
        result.append(chr((ord(ii)-ord("a")+i)%26+ord("a")))
    print ''.join(result)