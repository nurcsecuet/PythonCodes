# dict1 = {1:2, 2:3, 4:5}
# dict2 = dict1
#
# dict1[6] = 7
# print(dict1)
# print(dict2)

dict1 = {1:2, 2:3, 4:5}
dict2 = dict1.copy()
dict1[6] = 7
print(dict1)
print(dict2)