my_number = [2, 3, 1, 9, 7, 8]

def number(odd_even):
    if odd_even % 2 == 0:
        return "even"
    else:
        return "odd"

given_number = map(number, my_number)
print(next(given_number))
print(next(given_number))
print(next(given_number))
print(next(given_number))
print(list(given_number))