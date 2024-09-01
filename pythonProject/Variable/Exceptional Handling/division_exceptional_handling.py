try:
    n = int(input("Enter the numerator: "))
    d = int(input("Enter the denominator: "))

    division = n / d
    print(division)
except ZeroDivisionError:
    print("Division by zero error")  # program will not stop work. it will show message
except ValueError:
    print("Value Error")
else:
    print("No error found..")
finally:
    print("Ending message")
