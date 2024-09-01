mylist = [-5, -6, 200, -4000, -200, -3, -2]
min = mylist[0]
min_index = 0
length = len(mylist)
for x in range (length):
    if mylist[x] < min:
        min = mylist[x]
        min_index = x

print(min_index)
