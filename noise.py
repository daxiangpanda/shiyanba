#!/usr/bin/env python
# encoding: utf-8

from PIL import Image

box1 = (0,0,6,10)
box2 = (10,0,16,10)
box3 = (20,0,26,10)
box4 = (30,0,36,10)

def openim(path):
    return Image.open(path)
def print1(im):
    width = im.size[0]
    height = im.size[1]
    pix = im.load()
    # print pix
    result = []
    for x in range(width):
        for y in range(height):
            if pix[x,y] not in result:
                result.append(pix[x,y])
            # print l
    return result

def convert1(img):
    img = img.convert("L")
    WHITE, BLACK = 255, 0
    img = img.point(lambda x: WHITE if x >= 230 else BLACK)
    img = img.convert('1')
    return img

def cut(img):
    box1 = (0,0,6,10)
    box2 = (10,0,16,10)
    box3 = (20,0,26,10)
    box4 = (30,0,36,10)
    im1 = img.crop(box1)
    im2 = img.crop(box2)
    im3 = img.crop(box3)
    im4 = img.crop(box4)
    return im1,im2,im3,im4



def OCR(img):
    test1 = convert1(img)
    im1,im2,im3,im4 = cut(test1)
    result = []
    for i in range(10):
        if print1(im1) == font[i]:
            result.append(str(i))
    for i in range(10):
        if print1(im2) == font[i]:
            result.append(str(i))
    for i in range(10):
        if print1(im3) == font[i]:
            result.append(str(i))
    for i in range(10):
        if print1(im4) == font[i]:
            result.append(str(i))
    return int(''.join(result))




def getfont():
    font = []
    path = 'C:\\Users\\31351\\PycharmProjects\\shiyanba\\bmptest\\font\\'
    name = r'.bmp'

    for i in range(10):
    # path+str(i)+name
        im = openim(path+str(i)+name)
        font.append(print1(convert1(im)))
    return font

font = getfont()

path = 'C:\\Users\\31351\\PycharmProjects\\shiyanba\\bmp\\bmp\\'
sum = 0
for i in range(1,10000):
# sum = 0
    img = openim(path+str(i)+'.bmp')
    print path+str(i)+'.bmp'
    sum+=i*int(OCR(img))
    print 'sum ='+str(sum)