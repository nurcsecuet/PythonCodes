my_pointer = open("test_file.txt")

print(my_pointer.read(5))
print(my_pointer.read(4))
print(my_pointer.tell()) # tell is used to position of cursor
my_pointer.seek(0)  # move the cursor to zero position
print(my_pointer.tell())