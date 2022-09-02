import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
window.title("Tip Calculator")
window.mainloop()
#tip calculator
print("Welcome to the tip calculator")
print("Please enter the total bill amount")
bill = float(input())
print("Please enter the tip percentage")
tip = float(input())
print("How many people are splitting the bill")
people = float(input())
tip_amount = bill * (tip/100)
total_bill = bill + tip_amount
total_tip_per_person = tip_amount / people
total_bill_per_person = total_bill / people
print("The tip amount is $" + str(tip_amount))
print("The total bill is $" + str(total_bill))
print("The total bill per person is $" + str(total_bill_per_person))
print("The tip amount per person is $" + str(total_tip_per_person))
print("Thank you for using the tip calculator")
print("Goodbye")
#end of program