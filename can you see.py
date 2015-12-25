# # encoding: utf-8
#
# # import Image
# # import ImageEnhance
# # import ImageFilter
# import sys
# from pytesser import *
#
# # # 二值化
# threshold = 140
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# #
# # #由于都是数字
# # #对于识别成字母的 采用该表进行修正
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
#
# im = Image.open(r'E:\1.tif')
# imgry = im.convert('L')
# out = imgry.point(table,'1')
# textcode = image_to_string(im)
# print textcode
#
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
#
from PIL import Image

box1 = (0,0,6,10)
box2 = (10,0,16,10)
box3 = (20,0,26,10)
box4 = (30,0,36,10)

for i in range(1,17):
    path = 'E:\\shiyanba\\1225\\canyousee\\bmptest\\'+str(i)+".bmp"
    # print path
    im = Image.open(path)
    im.crop(box1).save('E:\\shiyanba\\1225\\canyousee\\bmptest\\'+str(i)+'01'+".bmp")
    im.crop(box2).save('E:\\shiyanba\\1225\\canyousee\\bmptest\\'+str(i)+'02'+".bmp")
    im.crop(box3).save('E:\\shiyanba\\1225\\canyousee\\bmptest\\'+str(i)+'03'+".bmp")
    im.crop(box4).save('E:\\shiyanba\\1225\\canyousee\\bmptest\\'+str(i)+'04'+".bmp")

def printrgb(im):
    width = im.size[0]
    height = im.size[1]
    for x in range(width):
        for y in range(height):
            r,g,b = pix[x,y]
            print r,g,b

二值化：


import numpy as np
from PIL import Image
import skimage.io

img = Image.open(file_name)
img = img.convert("L")

imgs = skimage.io.imread(file_name)
ttt = np.mean(imgs)

WHITE, BLACK = 255, 0

img = img.point(lambda x: WHITE if x > ttt else BLACK)
img = img.convert('1')
img.save(new_file_name)