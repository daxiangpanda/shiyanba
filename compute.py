__author__ = '31351'
for a in range(1,11):
    for b in range(1,11):
        for c in range(1,11):
            for d in range(1,11):
                for e in range(1,11):
                    for f in range(1,11):
                        for g in range(1,11):
                            for h in range(1,11):
                                for i in range(1,11):
                                    for j in range(1,11):
                                        if a != b and b!=c and c!=d and d!= e and e!=f and f!=g and g!=h:
                                            list1 = [a,b,c,d,e,f,g,h,i,j]
                                            list2 = []
                                            for i in list1:
                                                if i not in list2:
                                                    list2.append(i)
                                            if len(list2) ==10:
                                                a,b,c,d,e,f,g,h,i,j = list2
                                                if g+b+a == f+a+e and f+a+e == j+e+d and j+e+d == i+d+h and i+d+h == h+c+b:
                                                    print a,b,c,d,e,f,g,h,i,j
                                            # if g+b+a == f+a+e and f+a+e == j+e+d and j+e+d == i+d+h and i+d+h == h+c+b:
                                            #     print a,b,c,d,e,f,g,h,i,j
