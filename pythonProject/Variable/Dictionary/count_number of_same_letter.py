mylist = "programming in     python"
mymap = {}

for x in mylist:
    if x not in mymap:
        if x == " ":
            continue
        mymap[x] = 1
    else:
        mymap[x] += 1
print(mymap)