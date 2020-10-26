def address():
    keep_going = True
    while keep_going:
        address = input("Enter delivery address: > ")
        if address == '':
            print("Address cannot be blank. ")
        elif all(x.isalnum() or x.isspace() for x in address):
            keep_going = False
            return address


h=address()
print(h)