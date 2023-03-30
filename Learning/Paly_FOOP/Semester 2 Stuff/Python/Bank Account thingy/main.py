import BankAccount as ba

mySavings = ba.BankAccount(2500, "My Name", 10234652)
bellsSavings = ba.BankAccount(100000000, "Chris Bell", 1)

bellsSavings.changeInterestRate(.5)

mySavings.deposit(10000)

print(bellsSavings.withdraw(100))
print(bellsSavings.withdraw(10000))
print(mySavings.withdraw(20000))

print(bellsSavings.currentBalance())
print(mySavings.currentBalance())

print(vars(bellsSavings))
print(vars(mySavings))