
# try-except prevents a crash error
# https://docs.python.org/2/tutorial/errors.html


# True is always true; so loop for ever
while True:
    try:
        # Python 2.x users should use raw_input, the equivalent of 3.x's input
        user_input = input("Please enter your age: ")
        # try to convert to integer, this step may fail
        age = int(user_input)
    except ValueError:
        # if there is an error then do this
        print("Sorry, I didn't understand that.")
        continue
    else:
        # if there isn't an error then do this
        # this breaks out of the innermost loop
        break

print(age)



