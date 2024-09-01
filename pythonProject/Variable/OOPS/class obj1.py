# class student:
#     university="Latech"
#     welcome = "Welcome to our University"
#     print(welcome)
#     def __init__(self, name, roll, university):
#         self.name = name
#         self.roll = roll
#         self.university = university
#
#
# s1 = student("bright", 23, "UNCC")
# print(s1.name)
# print(s1.roll)
# print(s1.university)
# print(student.university)
#
# s2 = student("shekar", 20)
# print(s2.name)
# print(s2.roll)
# print(s2.university)

class student:
    university = "Latech"
    welcome = "Welcome to our University"
    print(welcome)
    def __init__(self, name, roll, university):
        self.name = name
        self.roll = roll
        self.university = university
s1 = student("bright", 23, "UNCC")
print(s1.name)
print(s1.roll)
print(s1.university)
print(student.university)
