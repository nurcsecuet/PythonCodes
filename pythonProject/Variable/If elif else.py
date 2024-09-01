a= 30
b = 30
c = 30

if a > b:
    if a > c:
        print (f"{a} is greatest")
elif b > a:
    if b > c:
        print(f"{b} is greatest")

elif c > a:
    if c > b:
        print(f"{c} is greatest")
else:
    print(f"{a, b, c} is Equal")

