a = ["ws", "bws", "amazon", "microsoft"]

max = a[0]
max_index = 0
for x in range (len(a)):
    if len(a[x]) > len(max):
        max = a[x]
        max_index = x

print(max)
print(x)