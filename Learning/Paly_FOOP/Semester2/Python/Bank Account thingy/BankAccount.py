class BankAccount:
    def __init__(self, balance, name, accountNumber):
        self.balance = balance
        self.name = name
        self.accountNumber = accountNumber
        self.interestRate = .05
    def currentBalance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return "Withdrawal Successful"
    def changeInterestRate(self, newInterestRate):
        self.interestRate = newInterestRate

