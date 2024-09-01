mylist = [1, 2, 3, 4]
mymap = {}
sum_key = 0
sum_value = 0

for x in mylist:
    mymap[x] = x*x
    sum_key = sum_key + x
    sum_value = sum_value + mymap[x]
print(mymap)
print(sum_key)
print(sum_value)
