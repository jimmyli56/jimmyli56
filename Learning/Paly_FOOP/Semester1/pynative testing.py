# # Exercise 2 
# s1 = "Ault"
# s2 = "Kelly"

# print(s1 + s2 + s1[2:])

# #Exercise 3 
# def mixed_string(s1, s2):
#     # get the first character from both string
#     first = s1[0] + s2[0]

#     # get the middle character from both string
#     middle = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

#     # get last character from both string
#     last= s1[len(s1) - 1] + s2[len(s2) - 1]

#     # adds all of them together
#     res = first_char + middle_char + last_char
#     print("The mixed string is ", res)

# s1 = "America"
# s2 = "Japan"
# mix_string(s1, s2)

# #Exercise 4

# str1 = "PyNaTive"
# print('Original String:', str1)
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         # adds lowercase characters to lower list
#         lower.append(char)
#     else:
#         # adds uppercase characters to lower list
#         upper.append(char)

# # Join both lists and print
# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)

# # Exercise 5

# def find_digits_chars_symbols(input_string):
#     digits = 0
#     chars = 0
#     symbols = 0
#     for i in range(len(input_string)):
#         if input_string[i].isdigit():
#             digits = digits + 1
#         elif input_string[i].isalpha():
#             chars = chars + 1
#         else:
#             symbols = symbols + 1
#     print("Digits", digits)
#     print("Chars", chars)
#     print("Symbols", symbols)
# input_string = "P@#yn26at^&i5ve"
# print("total counts of chars, Digits, and symbols \n")
# find_digits_chars_symbols(input_string)

# # Exercise 16

# str = 'I am 25 years and 10 months old'
# print("Original string is", str)
# result = "".join([item for item in str if item.isdigit()])
# print(result)