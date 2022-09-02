#tip calculator by Jimmy Li
print("Welcome to the tip calculator!")
print("Please enter the total bill amount.")
bill = float(input())
print("Please enter the tip percentage.")
tip = float(input())
print("How many people are splitting the bill?")
people = float(input())
tip_amount = bill * (tip/100)
total_bill = bill + tip_amount
total_tip_per_person = tip_amount / people
total_bill_per_person = total_bill / people 
print("The tip amount is $" + str(round(tip_amount, 2))+".")
print("The total bill is $" + str(round(total_bill,2))+".")
print("The total bill per person is $" + str(round(total_bill_per_person,2))+".")
print("The tip amount per person is $" + str(round(total_tip_per_person,2))+".")
print("Thank you for using the tip calculator! Have a nice day!")
#end of program
