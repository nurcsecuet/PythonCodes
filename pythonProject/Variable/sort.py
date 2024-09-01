mylist = [1, 2, 3.9, 3.5]
mylist.sort()
print(mylist)
print(type(mylist[1]))
mylist.sort(reverse = True)
print(mylist)

mylist.remove(3.5)
print(mylist)
mylist.pop(1)
print(mylist)

mylist = ["A", "z", "a", "B", "c", "C"]
mylist.sort(key = str.upper)
print(mylist)

list1 = [2, 3, 4, 5]
list2 = list1
list2.append(10)
print(list1)
list1 = [2, 3, 4]
list2 = list1.copy()
print(list1)
mylist = [1, 2, 3, 4, 5]
list2 = mylist[:]
list3 = mylist[2:3]
print(list2)
print(list3)

list4 = list2 + list3
print(list4)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

for x in list2:
    list1.append(x)

print(list1)

list1 = [2, 4, 6]
list2 = [7, 8, 9, 10, 11]

for x in list2:
    if x%2!=0:
        list1.append(x)

print(list1)
x = 100
if 0:
    print(x)
else:
    y = x+x
    print(y)


a = 100
b = 100

if a>b:
    print("a is greater")

elif a<b:
    print("b is greater")
else:
    print("a equals to b")



