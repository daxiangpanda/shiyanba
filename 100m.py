#!/usr/bin/env python
# encoding: utf-8
import urllib2
from bs4 import BeautifulSoup
# def url_open(url):
#     # url = urllib.quote(url)
#     req = urllib2.Request(url)
#     response = urllib2.urlopen(req)
#     html = response.read()
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup
#

#
# url = 'http://ctf8.shiyanbar.com/jia/'
# print process(url_open(url))


#coding:utf-8
import re,requests

def process(soup):
    a = soup.find("<div name='my_expr'>")+20
    # print a
    b = soup.find('</div>',a)
    # print b
    # eval 是什么鬼？
    #
    # print soup[a:b].replace('x','*')
    # print a
    # print b
    return soup[a:b].replace('x','*')

url = r"http://ctf8.simplexue.com/jia/"
session = requests.Session()
html = session.get(url).content
# print html
# print process(html)
#运用前向肯定断言和后向肯定断言匹配到网页源码内的算式
# pattern = re.compile(r"(?<=my_expr'>)(.*?)(?= )")
# match = pattern.search(html).group().replace('x','*')
#url对应页面里输入框的名字是pass_key，所以post的字典里得写明该键名,eval()计算表达式值
post = session.post(url,{'pass_key':eval(process(html))})
print post.content


