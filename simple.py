# booleans
# conditional: 'if else' statements
# fnum = input("what is the first number ")
# snum = input("what is the second number ")


    # What we have below us is the outline of 
    # a perfect conditional statement to template

# # if first number is bigger than do something
# # if second number is bigger, than do a different thing
# if fnum > snum:
#     print("the first number is bigger ")
# elif fnum < snum:
#     print("the second one is the larger-est ")
# else:
#     print("Clearly the numbers are even foo!")


# Write a program that prompts user to enter their score (out of 100) and 
# displays their corresponding grade based on the following criteria


    # Score 98 and above: Grade A
    # Score 88 to 89:  Grade B
    # Score 78 to 79:  Grade C 
    # Score 68 to 69:  Grade D
    # Scores less 68: Grade F

score = input("What was your test score?")
score = int(score)

if score >= 90:
    age = int(input("What is your age? "))
    if age < 10: # Nested if statement
        print("Your grade is an A++")
    else:
        print("Your grade is an A")
elif score >= 80:
    age = int(input("What is your age? "))
    if age < 10: # Nested if statement
        print("Your grade is an B++")
    else:
        print("Your grade is a B")
elif score >= 70:
    age = int(input("What is your age? "))
    if age < 10:
        print("Your grade is an C++")
    else: 
        print("Your grade is a C")
else:
    print("You must study more next time!")


