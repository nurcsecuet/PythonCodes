mymarks = [87, 88, 92, 93, 72, 67]

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "D"

mygrade = map(grade, mymarks)
print(next(mygrade))
print(next(mygrade))
print(next(mygrade))
print(next(mygrade))
print(next(mygrade))
print(next(mygrade))
print(list(mygrade))
