# # players = ["Mary","Chris","Atif","Chris","Lucy"]
# # count = 0
# # players.pop()
# # players.append("Bell")
# # players.remove("Mary")
# # players.remove("Chris")
# # players.insert(2,"Annabelle")
# # print(players)

# players = ["Mary","Chris","Atif","Annabelle","Lucy"]
# name = input("Enter a name (Case sensitive): ")
# if name in players:
#     print("Name found and removed.")
#     players.remove(name)
    
#     print(players)
# else:
#     print("Name not found, added to list.")
#     players.append(name)
#     print(players)

gpa_list = []
grade = 0
while grade != -1:
    grade = float(input("Enter a grade: "))
    if grade != -1:
        gpa_list.append(grade)
print(gpa_list)



