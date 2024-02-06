# with open('newfile.txt', mode='w') as file:
# same as below, except using only the letter and not 'mode' is short-hand
# or if we change the 'w' to 'a' we can append the file
# 'w' over-writes appended files so we will just over write the appened example
try:
    with open('sameple/newfile.txt', 'a') as file:
        # file.write("This is a new file we created!")
        file.writelines(["\nThis is a new file Chris from CialoneCodes created!", "\nThis is another line to be added by using the writelines"])
except FileNotFoundError as e:
    print("ERROR", e)

# exception above catches the forced error we made by searching for a file
# we know does not exist with the sameple/newfile