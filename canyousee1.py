# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import os
def logo_watermark(img):
    '''
    添加一个图片水印,原理就是合并图层，用png比较好
    '''
    baseim = Image.new ("RGBA", (60, 30), (255, 255, 255))
    logoim = Image.open(img)
    bw, bh = baseim.size
    lw, lh = logoim.size
    baseim.paste(logoim, (10,10))
    return baseim
for img in os.listdir("C:\\Users\\31351\\Downloads\\bmp\\bmp1\\"):
    address = "C:\\Users\\31351\\Downloads\\bmp\\bmp1\\"
    im = Image.open(address+img)
    im.show()
    vcode = pytesseract.image_to_string(im)
    print address+img+':'+vcode

