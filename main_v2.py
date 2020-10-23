# Imported things
from menu2 import menu

# Functions
def greeting():
    print("Welcome to Joe Nuts")


def display():
    for i in menu:
        b = menu[i]
        n = b["item"]
        l = b["price"]
        text = "${price}\t{item}".format(item=n, price=l)
        print(text)


def customer_name():
    a = 0
    while a != 1:
        try:
            name = input("Enter name: ")  # Initial input
            if not name.isalpha():  # Checks if name contains only characters
                print("Please enter only alphabetical characters for your name. ")
            else:
                a = 1
                return name
        except ValueError:
            print("Please enter a proper name")


def address():
    a = 0
    while a != 1:
        try:
            address = input("Enter delivery address: ")  #Initial input
            if address == "":
                print("Address cannot be blank. ")
            else:
                a = 1
                return address
        except ValueError:
            print("Please enter a proper name")


def phone():
    a = 0
    while a != 1:
        try:
            phone_number = int(input("Enter contact number: "))  # Initial input
            a = 1
            return phone_number
        except ValueError:
            print("Please enter a valid input")


def order():
    z = {}  # Test dictionary
    t = input("Would you like to make an order? If not please leave blank. ")
    while t != "":
        try:
            item = int(input("Please make a selection 1-12 of the menu (0 to finish order): "))
            if item >= 1 and item <= 12:
                quantity = int(input("How many: "))
                if quantity > 5:
                    print("Max order limit is 5. ")
                elif quantity == 0:
                    print("Item not added. ")
                else:
                    f = 'item'+str(item)  # Creates item search term
                    d = menu[f]  # Sets the order item to a variable
                    n = d['item']  # Pulls item name from dictionary
                    if f in z:
                        z[f] += quantity
                        order_out[n] += quantity
                    else:
                        z[f] = quantity  # Sends to the list used for calc
                        order_out[n] = quantity  # Sends to the list to display order
                
            elif item == 0:
                return z
        except ValueError:
            print("Not a valid input.")


def check():
    for i in customer_order:
        if customer_order[i] > MAX:
            print(customer_order[i],"was over the limit of 5. Put order quanity to 5 for convinience.")
            customer_order[i] = MAX
            print(i,customer_order[i])
    return customer_order


def calc(bruh):
    z = sum([menu[b]["price"]*bruh[b] for b in bruh.keys()])
    return z


def confirm():
    print('\n'.join("{}: {}".format(k, v) for k, v in order_out.items()))
    print("Total Cost: $"+str(total_cost))
    edit = input("Would you like to edit your order? y/n ").lower()
    while edit not in ("y","n"):
        edit = input("Would you like to edit your order? y/n ").lower()
    if edit == "n":
        print("Finalising order.")
        print("Order for", name, "> Deliver to", address, "> Contact No.", phone, "\nTotal Order Cost: $"+str(total_cost))
        print('\n'.join("{}: {}".format(k, v) for k, v in order_out.items()))
        print("Total Cost: $"+str(total_cost))
    elif edit == "y":
        return edit


def change(skin):
    if skin == "n":
        print("Finalising order. ")
    elif skin == "y":
        a = input("What item would you like to change? > ")
        while a not in (order_out):
            a = input("What item would you like to change? > ")
        b = int(input("How many would you like? > "))
        order_out[a] = b
        print(order_out)




MAX = 5  # Constant for order limit for each item
order_out = {}  # Dictionary to display the customers order

# Main program

greeting()
name = customer_name()
address = address()
phone = phone()
display()  # Displays the menu
while True:
    customer_order = order()  # Gets the customers order
    order_check = check()  # Checks if anything is over the limit
    total_cost = calc(order_check)  # Price calculation
    order_confirm = confirm()
    change(order_confirm)
    cont = input("Would you like to make another order? y/n > ").lower()
    while cont not in ("y", "n"):
        cont = input("Would you like to make another order? y/n > ").lower()
    if cont == "n":
        break
