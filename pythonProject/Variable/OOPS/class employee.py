class employee:
    def __init__(self, my_name, my_id, my_position, department, salary):
        self.name = my_name
        self.id = my_id
        self.position = my_position
        self.department = department
        self.salary = salary

s1 = employee("nur", 23, "manager", "engineering", 100000)
print(s1.name)
print(s1.position)
print(s1.salary)

s2 = employee("bright", 24, "executive", "HR", 120000)
print(s2.name)
print(s2.position)
print(s2.salary)
