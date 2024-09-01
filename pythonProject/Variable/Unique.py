l1 = [1, 1, 2, 2, 2, 3, 3, 5, 5, 6, 6, 7, 7, 7]

l2 = []
index = 0
while index < len(l1):
    if l1[index] not in l2:
        l2.append(l1[index])
        index += 1
    else:
        index += 1
print(l2)

l3 = [1, 2, 3, 4, 5, 6]
l4 = []
index = 0
while index < len(l3):
    if l3[index] in l4:
        print("Duplicate")
        break
    else:
        l4.append(l3[index])
        index +=1
if index == len(l3):
    print("Unique")
