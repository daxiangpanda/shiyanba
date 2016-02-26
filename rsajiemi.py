#!/usr/bin/env python
# encoding: utf-8

def RSA_jiemi(d,n,tep):
    M = []
    for i in tep:
        M.append(pow(ord(i),d,n))
    a = ''
    for i in M:
        a = a+chr(i)
    print '明文为'+a

d = int(-8730308722699440266242004151424821643188289931193109699825281130682946193055L)
p = 286924040788547268861394901519826758027
q = 258631601377848992211685134376492365269
n = p*q

with open('E:\\shiyanba\\1230\\RSA\\RSA\\flag.enc','r') as f:
    tep = f.read()
RSA_jiemi(d,n,tep)