mystring = input("Enter the string: ")

vowel = ["a", "e", "i", "o", "u"]

count = 0

for x in mystring:
    if x in vowel:
        count += 1
print(count)