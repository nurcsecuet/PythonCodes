class student:
    def __init__(self, email, pasword):
        self.email = email
        self.__password = pasword

s1 = student("nurchowdhury121@gmail.com", "ruston@321")
print(s1.email)
print(s1.password)