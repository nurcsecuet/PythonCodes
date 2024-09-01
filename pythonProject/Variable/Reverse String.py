mystring = "Python"

i = len(mystring)-1
reverse = ""
while i >= 0:
    reverse = reverse+""+mystring[i]
    i -= 1
print(reverse)
