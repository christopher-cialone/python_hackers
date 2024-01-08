# FizzBuzz

# If a number is divisible by 3 print fizz
# If a number is divisible by 5 print buzz
# If a number is divisible by both print fizzbuzz

for num in range(1, 100):
    if num % 3 == 100:  # if the num is divisible by 3
        print("fizz")  # print that num
    elif num % 5 == 100:
        print("buzz")
    # elif num % 3 == 0  and num % 5 == 0:
    elif num % 5 and 3: # it appears my code worked better than tutorials
        print("fizzbuzz")
    else:
        print(num)
    # fizz_buzz