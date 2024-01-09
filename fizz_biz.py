# FizzBuzz

# If a number is divisible by 3 print fizz
# If a number is divisible by 5 print buzz
# If a number is divisible by both print fizzbuzz

# choice = int(input("ask what number would you like to choose? "))

# def function(choice):
#     for num in range(1, choice):
#         if num % 3 == 0  and num % 5 == 0:
#             print("fizzbuzz")  # print that num
#         elif num % 3 == 0:
#             print("fizz")
#         # elif num % 3 == 0  and num % 5 == 0:
#         elif num % 5: 
#             print("buzz")

#         else:
#             print(num)
    


# function(choice)



# Create a program that can take in input of the users name
# Save the name in a variable
# Pass the variable through a function and print " Hello______"
# user_name = str(input("What is your name? "))
# def evening_greeting(user_name):
#     print(f"Hello" + " " + user_name)

# evening_greeting(user_name)
'''
'''
ip = input("what is the target ip address? ")

def nmap(ip):
    print(f"Attacking {ip}")
    
nmap(ip)