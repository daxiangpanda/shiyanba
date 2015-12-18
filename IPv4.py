#!/usr/bin/env python
# encoding: utf-8

# with open('E:\BaiduYunDownload\delegated-apnic-20140223','r') as f:
#     for line in f:
#         line = f.readline()
#         print line
result = 0
f = open('E:\BaiduYunDownload\delegated-apnic-20140223','r')
for line in open('E:\BaiduYunDownload\delegated-apnic-20140223'):
    line = f.readline()
    if line.startswith('apnic') and line.split('|')[2] == 'ipv4' and line.split('|')[1] == 'CN':
        result+=int(line.split('|')[4])
print result