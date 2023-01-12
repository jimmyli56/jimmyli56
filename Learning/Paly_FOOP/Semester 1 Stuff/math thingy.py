import math
mode=input("What mode do you want to use? (1) feet to inches or (2) inches to feet? ")
if mode == "1":
    feet=input("How many feet do you want to convert to inches? ")
    print(feet + " feet is " + str(int(feet)*12) + " inches.")
elif mode == "2":
    inches=input("How many inches do you want to convert to feet? ")
    print(inches + " inches is " + str(int(inches)/12) + " feet.")
else:
    print("Invalid mode.")
print("Thank you for using the unit converter, Goodbye.")