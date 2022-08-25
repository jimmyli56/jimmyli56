#tip calculator
print("Welcome to the tip calculator")
print("Please enter the total bill amount")
bill = float(input())
print("Please enter the tip percentage")
tip = float(input())
tip_amount = bill * (tip/100)
total_bill = bill + tip_amount
print("The tip amount is $" + str(tip_amount))
print("The total bill is $" + str(total_bill))
print("Thank you for using the tip calculator")
print("Goodbye")
#end of program