mylist = [1, 2, 3, 0, 4, 5]

for x in mylist:
    if x == 0:
        break
    print(x)

mylist = "Latech"
for i in range(len(mylist)):
    print(mylist[i])


mylist = "Latech"
for x in mylist:
    print(x)

mylist = [1, 2, 3, 0, 4, 5]

for x in mylist:
    if x == 0:
        continue  #Skip then continue
    print(x)