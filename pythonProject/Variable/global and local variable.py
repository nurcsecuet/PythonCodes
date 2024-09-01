x = 20
def myfun():
        print(x)

myfun()

x = 20
print(x==20)
print(x!=20)
print(x<=100)
print(x>=50)

a = "Hello World"
print("Hell" in a)

a = [10, 20, 30, 40]
print(10 in a)

x = 7
y = 5
print(x&y)
x = 7
y = 5
print(x|y)
x = 7
y = 5
print(x^y)
x = 7
print(~x)
x=-8
print(bin(x))

x = 7
print(x << 2)
x = 7
print(x >> 2)

print('It\'s "Morning"')

fruits = "mango, apple, cherry"
print(fruits)
print(fruits.split(", "))

a = "Hello"
b = "World"
print(a+b)
print(a+" "+b)

age = 15
a = "what are you doing"
b = "who are you"
print(a + "go ahead " +b)

txt = "abcd" + "echo"
print(txt)

age = 15
print(f"My age is {age}")

a = 20
b = 40

if a > b:
        print("a is greater")
else:
        print("b is greater")
print(bool(0))
print(bool(-1))
print(bool(None))
print(bool(""))
print(bool([]))
mylist = [1, 2, 3, 4, 5]
print(len(mylist))
print(type(mylist))
print(5 in mylist)
if 6 in mylist:
        print("Yes")
else:
        print("No")

mylist[1:3] = [200, 300]
print(mylist)
mylist[2] = [200, 300, 400]
print(mylist)
mylist[1:4] = [100]
print(mylist)
mylist.insert(1, 200)
print(mylist)
a = [1, 2, 3, 4, 5]
a.append(5)
print(a)
a.remove(4)
print(a)
print(len(a))
# a.remove(value) to remove value, a.pop(position) to remove value of that position, both are same
mylist = [1, 2, 3, 4, 5]
del mylist[2]
print(mylist)
mylist = [1, 2, 3, 4, 5]
mylist.clear()
print(mylist)
# del and clear are almost same, del delete whole list, clear cleared all value but still empty list is there

mylist = [1, 2, 3, 4]
for x in mylist:
        print(x)

print(range(10))
mylist = [10, 20, 30, 40, 50, 60]
length = len(mylist)
for i in range(length):
        print(mylist[i])

mylist = [10, 200, 30, 40, 3000]
max = 10
length = len(mylist)
for x in mylist:
        if (x > maximum):
                maximum = x
print(maximum)


