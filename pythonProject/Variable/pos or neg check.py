L1 = [-1, 1, 2, -2, -5, 5, -6, 6, 7, -7, -100]

pos = 0
neg = 0
i = 0
while i < len(L1):
    if L1[i] >= 0:
        pos = pos + 1
    else:
        neg = neg + 1
    i += 1

print("Number of positive number:", pos)
print("Number of negative number:", neg)
