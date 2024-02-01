# First we declare a variable called str
# Recall that string in Python is a sequence
# Because a string is a sequence it can be iterated over
# A sequence is just an ordered set
# The variable item is essentially just a plaeholder that will store the current letter in sequence
# You can access any character in the sequence by its INDEX

# For Loop

# str = 'Looping'

# for item in str:
#     print(item)


favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Turamisu', 'Ice-Box Cake']

for idx, item in enumerate(favorites):
    print(idx, item)

# idx is typically short for INDEX

# count = 0

# while count < len(favorites):
#     print('I like this desert', favorites[count])
#     count += 1