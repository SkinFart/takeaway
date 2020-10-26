def phone():  # Tested, this is better than using try/except, better formatting for user
    keep_going = True
    while keep_going:
        phone = input("Enter contact number: > ")
        if phone == '':
            print("Contact number cannont be blank. ")
        elif all(x.isnumeric() or x.isspace() for x in phone):
            keep_going = False
            return phone
        else:
            print("Please enter a valid input. ")

h=phone()
print(h)