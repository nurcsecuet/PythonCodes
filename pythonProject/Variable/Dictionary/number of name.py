name = ["john smith", "john Carly", "NUr Chowdhury"]
mymap = {}
for x in name:
    splitedname = x.split()
    first_name=splitedname[0]
    if first_name in mymap:
        mymap[first_name] += 1
    else:
        mymap[first_name] = 1
print(mymap)

