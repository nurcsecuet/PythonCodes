a = float(input("Enter triangle side a: "))
b = float(input("Enter triangle side b: "))
c = float(input("Enter triangle side c: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print ("Its a triangle")
else:
    print("Its not a triangle")