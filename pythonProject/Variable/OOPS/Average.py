class result:
    university = "Latech"
    state = "LA"
    def __init__(self, name, id, marks1, marks2, marks3):
        self. name = name
        self. id = id
        self. marks1 = marks1
        self. marks2 = marks2
        self.marks3 = marks3

    def myfunc(self):
        average = (self.marks1 + self.marks2 + self.marks3)/3
        return average

s1 = result("bright", 22, 91, 92, 93)
s1.myfunc()
print("Welcome to Latech, come and meet with Minardi")
print(s1.university)
print(s1.state)
print("Your average mark is: ", s1.myfunc())



