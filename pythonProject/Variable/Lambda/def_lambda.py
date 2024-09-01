def myfunc(n):
    return lambda a: a*n

x = myfunc(5)
print(x(2))