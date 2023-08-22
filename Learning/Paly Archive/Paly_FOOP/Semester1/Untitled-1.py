#dog age calculator
import math
def dog_age_calculator():
    dog_age = int(input("Enter the dog's age: "))
    human_age = 0
    if dog_age <= 2:
        human_age = dog_age * 10.5
    else:
        human_age = 21 + (dog_age - 2) * 4
    print("The dog's age in human years is", human_age)
dog_age_calculator()


