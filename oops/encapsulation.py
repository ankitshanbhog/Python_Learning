class BankAccount():
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance += amount

account = BankAccount(5000)

print(account.get_balance())
account.deposit(1000)
print(account.get_balance())