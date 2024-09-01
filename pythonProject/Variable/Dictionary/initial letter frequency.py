words = ["apple", "banana", "cherry", "pinaple", "blueberry"]

mymap = {}
for x in words:
    first_letter= x[0]
    if first_letter not in mymap:
        mymap[first_letter] = 1
    else:
        mymap[first_letter]+=1
print(mymap)