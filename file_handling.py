# assigning avariable to the 'with open' function
with open('test.txt', mode = 'r') as file:
    data = file.readline()
    print(data)

# open function has access to the test.txt file
# file = open('test.txt', mode = 'r')


# variable assigned to read file
# data = file.readline()

# print(data)

# 
# file.close()