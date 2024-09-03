dict = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6]

mymap = {}
for x in dict:
    if x not in mymap:
        mymap[x] = 1
    else:
        mymap[x] = mymap[x] + 1
print(mymap)

max = 0
for x in mymap:
    if mymap.get(x)>max:
        max = mymap.get(x)
        max_key=x
print(max)
print(max_key)
print(mymap.get(max_key))

print("I have made new changes after pushing the code to Github main")
print("i am in dev branch")
print("new changes")