# encoding: utf-8

import Image
import ImageEnhance
import ImageFilter
import sys
from pytesser import *

# # 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
#
# #由于都是数字
# #对于识别成字母的 采用该表进行修正
# rep={'O':'0',
#     'I':'1','L':'1',
#     'Z':'2',
#     'S':'8'
#     };
#
# def  getverify1(name):
#
#     #打开图片
#     im = Image.open(name)
#     #转化到亮度
#     imgry = im.convert('L')
#     imgry.save(r'E:\\BaiduYunDownload\\bmp.tar\\bmp\\'+'g'+name.split('\\')[-1])
#     #二值化
#     out = imgry.point(table,'1')
#     out.save(r'E:\\BaiduYunDownload\\bmp.tar\\bmp\\'+'b'+name.split("\\")[-1])
#     #识别
#     text = image_to_string(out)
#     #识别对吗
#
#     print text
#     return text
# getverify1(r'E:\BaiduYunDownload\bmp.tar\bmp\1.bmp')

im = Image.open(r'C:\Users\31351\PycharmProjects\shiyanba\30.tif')
imgry = im.convert('L')
out = imgry.point(table,'1')
textcode = image_to_string(out)
print textcode

# def logo_watermark(img):
#     '''
#     添加一个图片水印,原理就是合并图层，用png比较好
#     '''
#     baseim = Image.new ("RGBA", (60, 30), (255, 255, 255))
#     logoim = Image.open(img)
#     bw, bh = baseim.size
#     lw, lh = logoim.size
#     baseim.paste(logoim, (10,10))
#     baseim.save(r'E:\\BaiduYunDownload\\bmp.tar\\bmp\\'+'a.jpg','JPEG')
#     print u'logo水印组合成功'
# img = r'E:\BaiduYunDownload\bmp.tar\bmp\1.bmp'
# logo_watermark(img)