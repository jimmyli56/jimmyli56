mail = open('mail.txt')
counter = 0 
for line in mail:
    counter += 1
print(counter)
mail.seek(2000)
mail.close