def tuple_update_element():
    global tuple1
    mylist = list(tuple1)
    mylist[2] = 700
    tuple1 = tuple(mylist)

def tuple_delete_element():
    global tuple1
    mylist = list(tuple1)
    mylist.remove(10)
    tuple1 = tuple(mylist)
def tuple_add_element():
    global tuple1
    mylist = list(tuple1)
    mylist.append(12)
    tuple1 = tuple(mylist)

tuple1 = (5, 6, 7, 8, 9, 10)
tuple_update_element()
print(tuple1)
tuple_delete_element()
print(tuple1)
tuple_add_element()
print(tuple1)



