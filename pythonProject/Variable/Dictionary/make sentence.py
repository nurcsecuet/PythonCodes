my_dict = {1: 'I', 2: 'My', 3: 'love', 4: 'mom', 5:'you', 6:'my', 7:'Bangladesh', 8:'teacher'}
even = ""
odd = ""
for x in my_dict:
    if x % 2 == 0:
        even=even+my_dict[x]+" "
    else:
        odd = odd + my_dict[x] + " "
print("Even key:", even)
print("Odd Key:", odd)
