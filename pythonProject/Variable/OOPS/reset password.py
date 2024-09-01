class student:
    def __init__(self, email, pasword):
        self.email = email
        self.__password = pasword

    def resetpwd(self, newpwd):
        s1.__password = newpwd
    def displaypwd(self):
        print(self.__password)

s1 = student("nurchowdhury121@gmail.com", "ruston@321")
print(s1.email)
# print(s1.password)
s1.resetpwd("bright@123")
# print(s1.password)
s1.displaypwd()
