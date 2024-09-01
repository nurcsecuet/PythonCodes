veggie = ["carrot", "potato", "spinach", "carrot", "cabbage", "cauliflower", "ginger", "garlic", "garlic", "garlic"]

mymap = {}

for x in veggie:
    if x in mymap:
        mymap[x] += 1
    else:
        mymap[x] = 1
print(mymap)
max = 0
for x in mymap:
    if mymap.get(x) > max:
        max = mymap.get(x)
        max_key = x
print(max)
print(max_key)