mylist1 = [1, 2, 3, 3, 4, 4, 5]
mylist2 = []

i = 0
while i < len(mylist1):
    if mylist1[i] not in mylist2:
        mylist2.append(mylist1[i])
        i += 1
    else:
        i +=1
print(mylist2)