def credit (crdeit_amount):
    global account_balance
    account_balance = account_balance + crdeit_amount
    print(f"{crdeit_amount} was credited in your account and your new balance is {account_balance}")

def debit (debit_amount):
    global account_balance
    account_balance = account_balance - debit_amount
    print(f"{debit_amount} was debited from your account and your new balance is {account_balance}")

account_number = input("Enter your account number: ")
account_balance = int(input("Enter your account balance: "))

credit (20)
credit (40)
debit(10)
debit(50)
print(account_balance)

