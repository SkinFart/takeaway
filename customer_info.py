name = input("Enter your name: ")
if not name.isalpha():
    print("Please enter only alphabetical characters for your name.")
elif name.isdigit():
    print("Your name cannot be a number.")