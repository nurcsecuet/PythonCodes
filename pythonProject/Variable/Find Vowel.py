mystring = input("Enter the word: ")
vowels = ["a", "e", "i", "o", "u"]

count = 0
i = 0
while i < len(mystring):
    if mystring[i] in vowels:
        count = count + 1
    i += 1
print(count)