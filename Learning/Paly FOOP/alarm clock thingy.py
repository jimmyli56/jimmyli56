day=input("What day do you want to set the alarm for?".lower())
if ((day == "monday") or (day == "tuesday") or (day == "thursday") or (day == "friday")):
    print("your alarm is set for " + "8 AM.")
elif day == "saturday" or "sunday":
    print("your alarm is set for " + "10AM.")