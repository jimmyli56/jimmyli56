print ("Hello, What is your name?")
name = input()
print ("Hello, " + name + "!")
print ("What subject are you going to?")
subject = input()
if subject == "math" or subject == "Math":
    print ("Head to the 800 building, " + name)
elif subject == "science" or subject == "Science":
    print ("Head to the 1700 building, " + name)
elif subject == "english" or subject == "English":
    print ("Head to the 200 building, " + name)
elif subject == "pe" or subject == "PE":
    print ("Head to the Gym, " + name)
else:
    print ("Sorry, I dont know where that is, " + name)