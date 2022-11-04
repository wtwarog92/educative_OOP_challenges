#Inheritance Challenge 1

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

account1 = Account("Mark", 5000)


#Inheritance Challenge 2

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount
        pass

    def deposit(self, amount):
        self.balance += amount
        pass

    def getBalance(self):
        return self.balance
        pass


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return ((self.interestRate * self.balance)/100)
        pass
