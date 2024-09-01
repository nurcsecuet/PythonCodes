veggie = ["carrot", "potato", "spinach", "cabbage", "cauliflower", "garlic"]
mymap = {}
max = 0
for x in veggie:
    mymap[x] = len(x)
    if mymap.get(x)>max:
        max = mymap.get(x)
        max_key=x
print(max_key)

    
