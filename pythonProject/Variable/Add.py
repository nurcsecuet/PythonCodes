mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evensum = 0
oddsum = 0
for x in mylist:
    if x%2 == 0:
        evensum = evensum + x
    else:
        oddsum = oddsum + x

print(evensum)
print(oddsum)

print("we are learning python")