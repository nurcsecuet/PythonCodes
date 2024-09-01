marks = [32, 42, 50, 60, 75, 80, 90]

def myfunc(marks):
    return marks < 60

field = filter (myfunc, marks)
print(next(field))
print(next(field))
print(next(field))
print(list(field))