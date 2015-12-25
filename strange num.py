#!/usr/bin/env python
# encoding: utf-8

#coding:utf-8

import hashlib

def md5(s):
    return hashlib.md5(s).hexdigest()

def evalCrossTotal(strMd5):
    r = 0
    for i in strMd5:
        r += int("0x%s" % i, 16)
    return r

def encryptString(strString, strPasswd):
    strPasswdMd5 = md5(strPasswd)
    intMd5       = evalCrossTotal(strPasswdMd5)
    print intMd5
    r = []

    for i in range(len(strString)):
        r.append(
            ord(strString[i]) + \
            int("0x%s" % strPasswdMd5[i%32], 16) - \
            intMd5
        )
        # print md5(strString[:(i+1)])[:16]
        # print md5(str(intMd5))[:16]
        intMd5 = evalCrossTotal(
            md5(strString[:(i+1)])[:16] + \
            md5(str(intMd5))[:16]
        )
        # print intMd5
    # print r
    return " ".join(map(lambda x: str(x), r))

s = 'KEY'

print encryptString(s,'19910')