# Lucky sum thingy
print("Welcome to the lucky sum calculator!")
print("Please enter the first number.")
first = float(input())
print("Please enter the second number.")
second = float(input())
print("Please enter the third number.")
third = float(input())
if first == 13:
    print("The sum is 0.")
elif second == 13:
    print("The sum is " + str(first) + ".")
elif third == 13:
    print("The sum is " + str(first + second) + ".")
else:
    print("The sum is " + str(first + second + third) + ".")
print("Thank you for using the lucky sum calculator!")
