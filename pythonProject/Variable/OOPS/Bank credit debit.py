class bank_account:
    bank_name = "Chase"
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def debit(self, debit_amount):
        self.balance = self.balance-debit_amount
        print(f"Hi {self.name}, here is your mini statement")
        print("Your account debited by: ",debit_amount)
        print("Your new Balance is: ", self.balance)

    def credit(self, credit_amount):
        self.balance = self.balance + credit_amount
        print(f"Hi Bright, here is your mini statement")
        print("Your account credited by: ",credit_amount)
        print("Your new Balance is: ", self.balance)

s1 = bank_account("bright", "123456", 1000)
s1.debit(10)
# s1.credit(90)
s2 = bank_account("shekar", "9876543", 999)
# s2.debit(9)
s2.credit(99)


