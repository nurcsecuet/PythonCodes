def myfun(list2):
    sum = 0
    i = 0
    while i<len(list2):
        sum += list2[i]
        i = i+1
    return sum


list1 = [100, 200, 300, 400]
print(myfun(list1))