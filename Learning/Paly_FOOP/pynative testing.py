# # Exercise 2 
# s1 = "Ault"
# s2 = "Kelly"

# # expected result: AuKellylt
# print(s1 + s2 + s1[2:])

# #Exercise 3 
# def mixed_string(s1, s2):
#     # get the first character from both string
#     first_char = s1[0] + s2[0]

#     # get the middle character from both string
#     middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

#     # get last character from both string
#     last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

#     # adds all of them together
#     res = first_char + middle_char + last_char
#     print("The mixed string is ", res)

# s1 = "America"
# s2 = "Japan"
# mix_string(s1, s2)

#Exercise 4

str1 = "PYnAtivE"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # adds lowercase characters to lower list
        lower.append(char)
    else:
        # adds uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)


