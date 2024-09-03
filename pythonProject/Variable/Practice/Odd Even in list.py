mylist = [10, 11, 12, 13, 14, 17, 19, 21, 44, 45, 67, 68]

odd_list = []
even_list = []
sum_odd = 0
sum_even = 0
count_odd = 0
count_even = 0

i = 0
while i < len(mylist):
    if mylist[i] % 2 == 0:
        even_list.append(mylist[i])
        sum_even = sum_even + mylist[i]
        count_even = count_even + 1
    else:
        odd_list.append(mylist[i])
        sum_odd = sum_odd + mylist[i]
        count_odd = count_odd + 1
    i += 1
print(odd_list)
print(sum_odd)
print(len(odd_list))
print(even_list)
print(sum_even)
print(len(even_list))