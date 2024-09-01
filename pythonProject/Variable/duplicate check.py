def myfunc(mylist):
    set1 = set()

    for x in mylist:
        if x in set1:
            return True
        else:
            set1.add(x)
    return False
mylist1 = [1, 2, 3, 4, 5]
print(myfunc(mylist1))


