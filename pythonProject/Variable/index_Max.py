
mylist = [200, 400, 32, 5000, 450, 600, 420, 300]
max = 200
max_index = 0
length = len(mylist)
for x in range(length):

    if mylist[x] > max:
        max = mylist[x]
        max_index = x
print(max)
print(max_index)



