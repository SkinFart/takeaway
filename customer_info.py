
def customer_name():
    keep_going = True
    while keep_going:
        name = input("Name for order: > ")
        if name == '':
            print("Please enter a valid input")
        elif all(x.isalpha() or x.isspace() for x in name):
            keep_going = False
            return name
g=customer_name()
print(g)
