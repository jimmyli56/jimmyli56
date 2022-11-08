# Tip calculator by Jimmy Li

# Welcome message
print("Welcome to the tip calculator!")
print("Please enter the total bill amount.")
# Sets bill to inputted value
bill = float(input())
print("Please enter the tip percentage.")
# Sets tip to inputted value
tip = float(input())
print("How many people are splitting the bill?")
# Sets people to inputted value 
people = float(input())
# Calculates tip amount
tip_amount = bill * (tip/100)
total_bill = bill + tip_amount
total_tip_per_person = tip_amount / people
total_bill_per_person = total_bill / people 
# Prints tip amount, total bill, total bill per person and total tip per person, with everything rounded to 2 decimal places
print("The tip amount is $" + str(round(tip_amount, 2))+".")
print("The total bill is $" + str(round(total_bill,2))+".")
print("The total bill per person is $" + str(round(total_bill_per_person,2))+".")
print("The tip amount per person is $" + str(round(total_tip_per_person,2))+".")
print("Thank you for using the tip calculator!")
#end of program
