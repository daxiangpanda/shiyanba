#!/usr/bin/env python
# encoding: utf-8

import re,requests

def process(html):
    a = soup.find("<div name='my_expr'>")+20
    b = soup.find('</div>',a)
    return soup[a:b].replace('x','*')
# num1 =
# num2 =
num0 = r'&nbsp;xxx&nbsp;<br>x&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;x<br>&nbsp;xxx&nbsp;<br>'
num1 = r'&nbsp;xx<br>&nbsp;&nbsp;x&nbsp;x&nbsp;&nbsp;<br>&nbsp;&nbsp;x&nbsp;&nbsp;<br>&nbsp;&nbsp;x&nbsp;&nbsp;<br>xxxxx<br>'
num2 = r'&nbsp;xx<br>&nbsp;&nbsp;x&nbsp;x&nbsp;&nbsp;<br>&nbsp;&nbsp;x&nbsp;&nbsp;<br>&nbsp;&nbsp;x&nbsp;&nbsp;<br>xxxxx<br>'
num3 = r''
num4 = r'&nbsp;x&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;x<br>&nbsp;xxxxx<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>&nbsp;&nbsp;&nbsp;&nbsp;x<br>'
num5 = r'xxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;xxxx<br>&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxx<br>'

url = r"http://ctf4.shiyanbar.com/ppc/acsii.php"
session = requests.Session()
html = session.get(url).content.replace('<br/>','<br>').replace('<br />','<br>')
with open(r'html1.html','w') as f:
    f.write(html)
print html
# print html
# print process(html)
#运用前向肯定断言和后向肯定断言匹配到网页源码内的算式
# pattern = re.compile(r"(?<=my_expr'>)(.*?)(?= )")
# match = pattern.search(html).group().replace('x','*')
#url对应页面里输入框的名字是pass_key，所以post的字典里得写明该键名,eval()计算表达式值
# post = session.post(url,{'pass_key':eval(process(html))})
# print post.content