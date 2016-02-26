#!/usr/bin/env python
# encoding: utf-8

import re,requests,base64

url = r'http://ctf4.shiyanbar.com/web/10.php'
session = requests.Session()
html = session.get(url)

FLAG = html.headers['FLAG']

postcontent = base64.b64decode(FLAG).split(':')[1]

# print html
# print process(html)
#运用前向肯定断言和后向肯定断言匹配到网页源码内的算式
# pattern = re.compile(r"(?<=my_expr'>)(.*?)(?= )")
# match = pattern.search(html).group().replace('x','*')
#url对应页面里输入框的名字是pass_key，所以post的字典里得写明该键名,eval()计算表达式值
post = session.post(url,{'key':postcontent})
print post.content