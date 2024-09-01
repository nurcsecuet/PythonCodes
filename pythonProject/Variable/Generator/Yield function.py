def func():
    i = 0
    while i <= 10:
        yield i   #produce i
        i += 1

x = func()
print(next(x))
print(next(x))
