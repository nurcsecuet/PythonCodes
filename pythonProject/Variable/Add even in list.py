mylist = [2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlist = []
oddlist = []

for x in mylist:
    if x%2 == 0:
        evenlist.append(x)
    else:
        oddlist.append(x)

print(evenlist)
print(oddlist)
