# unique words
# open the file and read it line by line
with open('romeo.txt', 'r') as file:
    lines = file.readlines()

# initialize an empty list to store the unique words
unique_words = []

# split each line into a list of words and check if they are in the list of unique words
for line in lines:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

# sort the list of unique words in alphabetical order
unique_words.sort()

# print the list of unique words
print(unique_words)
