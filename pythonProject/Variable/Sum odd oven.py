mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = 0
sum_odd = 0
i = 0
while i < len(mylist):
    if mylist[i]%2 == 0:
        sum_even = sum_even + mylist[i]
    else:
        sum_odd = sum_odd + mylist[i]
    i +=1
print("The Sum Even is:", sum_even)
print("The Sum Odd is:", sum_odd)
