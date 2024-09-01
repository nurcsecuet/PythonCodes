Dictionary1 = {"laptop":5, "mobile":5, "watch":4}  #{key:value} # key must unique, value is not
# mylist= Dictionary1.keys()
# print(mylist)
# for x in mylist:
#     print(x)
Dictionary1["Television"]= 5
# Dictionary1.update({"Television":5}) #add element
# Dictionary1.pop("mobile") #remove specific element
print(Dictionary1)
Dictionary1.popitem()   #remove latest added element
print(Dictionary1)
del Dictionary1["laptop"]
print(Dictionary1)
Dictionary1.clear()
print(Dictionary1)
del Dictionary1
# print(Dictionary1)