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


# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Turamisu', 'Ice-Box Cake']

# for idx, item in enumerate(favorites):
#     print(idx, item)

# idx is typically short for INDEX

# count = 0

# while count < len(favorites):
#     print('I like this desert', favorites[count])
#     count += 1

# Controlling Loops - 
# Control Statements
    # Break
    # Continue
    # Pass

# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# for dessert in favorites:
#     if dessert == 'Pudding':
#         print('Yes one of my favorite desserts is', dessert) 
#     else:
#         print('No sorry, that dessert is not on my list')

# Loop Control Statements
# Break
# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# for dessert in favorites:
#     if dessert == 'Churros':
#         print('Yes one of my favorite desserts is', dessert)
#         break 
#     else:
#         print('No sorry, not a dessert on my list')

# import time
# start_time = time.time()
# '''Nested Loops'''
# # outer loop
# for x in range(450):
#     print(x)
#     # inner loop
#     for j in range(10):
#         print(0, end = " ")
#     print( )
# print(round((time.time() - start_time), 2))


    