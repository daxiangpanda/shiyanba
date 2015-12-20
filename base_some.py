from PIL import Image
Letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter = Letter.lower()
def main():
    temp = 'umfpbljhawrfrmxhz19zmf9megnrmw45x3donhq'
    length = len(temp)
    print length
    ans = ['0']*length
    number = [1,3,7,10,11,13,17,21,22,26,27,29,30,33,37,38,39]
    for i in range(length):
        print i+1 in number
        print temp[i]
        if i+1 in number:
            ans[i] = temp[i].upper()
        else:
            ans[i] = temp[i]
            # ans[i] = chr(ord(temp[i]-32))
        print ans
    print ''.join(ans)

if __name__ == '__main__':
    main()
