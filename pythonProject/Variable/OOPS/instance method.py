class student:
    university = "Latech"
    @classmethod
    def change_Uni_details(cls, new_university):
        cls.university = new_university

    def __init__(self, name, roll):  #Instance method
        self.name = name
        self.roll = roll

    def change_name(self, new_name):
        self.name = new_name

s1 = student("Jack", 22)
s1.change_Uni_details("ULM")
s1.change_name("Gill")
print(s1.name)
print(s1.university)
s2 = student("john", 100)
print(s2.name)
print(s2.university)