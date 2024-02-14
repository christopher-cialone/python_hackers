# some = ["aaa", "bbb"]

#1
# def aa(some):
#    return

# #2 - invalid syntax
# def aa(some, 5):
#    return

# #3
# def aa():
#    return

# #4
# def aa():
#    return "aaa"



numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)