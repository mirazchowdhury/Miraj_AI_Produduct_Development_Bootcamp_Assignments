def withdraw(balance,amount):
    if amount>balance:
        return "insufficient funds"
    else:
        new_balance = b-a
        return new_balance

a = float(input("Enter your amount: "))
b = 10000000.00000


c = withdraw(b,a)
print(c)
