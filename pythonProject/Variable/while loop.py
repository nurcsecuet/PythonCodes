l1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l2 = []

i = 0
while i < len(l1):
    if l1[i]%2==0:
        l2.append(l1[i])
    i += 1

print(l2)

l = ["a", "aws", "bp", "mango"]
i=0
max = l[i]
while i < len(l):
    if len(l[i]) > len(max):
        max = l[i]
    i += 1
print(max)


l3 = [10, 20, 30, 40, 50]

i = 0
sum = 0
while i < len(l3):
    sum = sum + l3[i]
    i +=1
print(sum)

l4 = [2, 3, 1, 1, 2, 1, 3, 1,1]

count = 0
i = 0
while i < len(l4):
    if l4[i] == 1:
        count +=1
    i +=1
print(count)

i = 110
while i < 121:
    print(i)
    i +=1

product = 1
i = 6
while i >= 1:
    product = product*i
    i=i-1

print(product)


