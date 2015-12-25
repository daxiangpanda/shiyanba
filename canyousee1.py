# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import ImageEnhance
import os
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

def  bina(img):
    imgry = img.convert('L')
    # imgry.save(r'E:\\BaiduYunDownload\\bmp.tar\\bmp\\'+'g'+name.split('\\')[-1])
    out = imgry.point(table,'1')
    # print out
    return out
def bigger(img):
    width,height = img.size
    # print width,height
    big = img.resize((120,30))
    # print big
    return big


def enhance(img):
    sharpness = ImageEnhance.Sharpness(img)
    sharp_img = sharpness.enhance(2.0)
    # print type(sharp_img)
    return sharp_img

def logo_watermark(img):
    '''
    添加一个图片水印,原理就是合并图层，用png比较好
    '''
    baseim = Image.new("RGBA", (360, 90), (255, 255, 255))
    logoim = img
    bw, bh = baseim.size
    lw, lh = logoim.size
    baseim.paste(logoim, (120, 30))
    # baseim.show()
    # print baseim
    return baseim
img1 = Image.open("E:\\shiyanba\\1.jpg")
vcode = pytesseract.image_to_string(logo_watermark(bigger(bina(img1))))
    # result = vcode.replace('n','0').replace('e','6').replace('E','8').replace('a','8').replace('m','0')
print vcode

