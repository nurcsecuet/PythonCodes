a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
op = input("Operation??: ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b


print(result)