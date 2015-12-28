#!/usr/bin/env python
# encoding: utf-8
import base64
import hashlib
import itertools


def check(src):
    m1 = hashlib.md5()
    m1.update(src)
    if m1.hexdigest() == '16478a151bdd41335dcd69b270f6b985':
        return True
    else:
        return False


def generate(word):
    n = len(word)
    tuple = [()]
    result = []
    for i in range(n):
        tuple.extend(list(itertools.combinations(range(n),i+1)))
    for i in tuple:
        result.append(change(word,i))
    return result


def change(word,tuple):
    b = list(word)
    result = []
    for i in range(len(b)):
        if b[i].isalpha():
            if i in tuple:
                result.append(word[i].lower())
            else:
                result.append(word[i])
        else:
            result.append(word[i])
    return ''.join(result)


def decrypt(word):
    for i in generate(word):
        if check(base64.b64decode(i)):
            return i
        else:
            print 'not '+ i

if __name__ == '__main__':
    word = 'YMFZZTY0D3RMD3RMMTIZ'
    result = decrypt(word)
    print 'flag is '+ base64.b64decode(result)