class student:
    name = "jack"
    roll = 23
    @classmethod
    def change_details(cls, name):
        cls.name = name


s1 = student()
print(s1.name)
s2 = student()
s2.change_details("John")
print(s2.name)
print(s1.name)