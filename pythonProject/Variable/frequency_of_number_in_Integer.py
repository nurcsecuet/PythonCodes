myint = 1221334
mymap = {}
while myint > 0:
    remainder = myint % 10
    if remainder not in mymap:
        mymap[remainder] = 1
    else:
        mymap[remainder] += 1
    myint = myint // 10
print(mymap)


