mylist1 = [1, 2, 3, 3, 4, 4, 5]
myset = set()

i = 0
while i < len(mylist1):
    if mylist1[i] not in myset:
        myset.add(mylist1[i])
        i += 1
    else:
        i +=1
print(myset)