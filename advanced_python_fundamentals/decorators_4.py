# STATIC METHOD

class Calculator:
    @staticmethod
    def add(a,b):
        return (a+b)
print(Calculator.add(10,20))

# CLASS METHOD

class School:
    name = "ABC College"

    @classmethod
    def change_name(cls,new_name):
        cls.name = new_name

School.change_name("XYZ College")
print(School.name)        

# PROPERTY METHOD

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance_info(self):
        return self.balance

account = BankAccount(5000)

print(account.balance_info)
