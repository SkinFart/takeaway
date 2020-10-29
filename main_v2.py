"""
The purpose of this program is to take a customers order from the takeaway chain Joe Nuts.

William Bigley
30/10/20
Version 2

"""


# Imported things
from menu2 import menu  # This is importint the menu dictionary from a different file


MAX = 5  # Constant for order limit for each item
order_out = {}  # Dictionary to display the customers order
loop = True  # Used for main loop


# Functions
def greeting():
    """The functions purpose is to welcome the customer."""
    print("Welcome to Joe Nuts")


def display():  # Done like this to make changes easy
    """The functions purpose is to display the menu."""
    for i in menu:
        b = menu[i]  # Id of dictionary for each item
        item = b["item"]  # This gets the item name
        number = b["id"]  # This gets the item id
        price = b["price"]  # This gets the price of the item
        text = "{id}.\t${price}\t{item}".format(item=item, price=price, id=number)  # This is what prints the menu
        print(text)


def customer_name():
    """The functions purpose is to get the order name."""

    keep_going = True
    while keep_going:
        name = input("Name for order: > ")
        if name == '':  # Checks if input is blank
            print("Please enter a valid input")
        elif all(x.isalpha() or x.isspace() for x in name):  # Checks that input only contains characters, no symbols etc
            keep_going = False
            return name
        else:
            print("Please enter a valid input. ")


def address():
    """The functions purpose is to get the customers delivery address."""

    keep_going = True
    while keep_going:
        address = input("Enter delivery address: > ")
        if address == '':  # Checks if input is blank
            print("Address cannot be blank. ")
        elif all(x.isalnum() or x.isspace() for x in address):  # Checks that input only contains characters and numbers, no symbols etc
            keep_going = False
            return address
        else:
            print("Please enter a valid input. ")


def phone():  # Tested, this is better than using try/except, better formatting for user
    """The functions purpose is to get the customers contact number."""

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


def order():
    """The functions purpose is to get the customers order."""

    order = {}  # Order dictionary
    t = input("Would you like to make an order? Max order limit 5. If not please leave blank. > ")
    if t == "":
        return {}
    while t != "":
        try:
            item = int(input("Please make a selection 1-12 of the menu (0 to finish order): > "))
            if item >= 1 and item <= 12:
                quantity = int(input("How many: "))
                if quantity > 5:
                    print("Max order limit is 5. ")
                elif quantity < 0:
                    print("Amount cannot be a negative value.")
                elif quantity == 0:
                    print("Item not added. ")
                else:
                    f = 'item'+str(item)  # Creates item search term
                    d = menu[f]  # Sets the order item to a variable
                    n = d['item']  # Pulls item name from dictionary
                    if f in order:
                        order[f] += quantity
                        order_out[n] += quantity
                    else:
                        order[f] = quantity  # Sends to the list used for calc
                        order_out[n] = quantity  # Sends to the list to display order

            elif item == 0:
                print("")
                return order
                order.clear()
        except ValueError:
            print("Not a valid input.")


def check():
    """The functions purpose is to check the order for anything over the limit,
        mainly from ordering the same thing more than once going over the limit that way."""

    for i in customer_order:
        if customer_order[i] > MAX:
            print(customer_order[i], "was over the limit of 5. Put order quanity to 5 for convinience.")
            customer_order[i] = MAX
            item = menu[i]["item"]
            order_out[item] = MAX
    return customer_order


def calc(bruh):
    """The functions purpose is to calculate the total order cost."""

    z = sum([menu[b]["price"]*bruh[b] for b in bruh.keys()])  # Calculates the total price
    return z


def confirm():
    """This functions purpose is to ask the user whether they want to edit their order or not."""

    print('\n'.join("{}: {}".format(k, v) for k, v in order_out.items()))  # Prints order to view
    print("Total Cost: $"+str(total_cost))
    if order_check == {}:
        return "n"
    edit = input("Would you like to edit your order? y/n > ").lower()
    while edit not in ("y", "n"):
        edit = input("Would you like to edit your order? y/n > ").lower()
    if edit == "n":
        return edit
    elif edit == "y":
        return edit


def change(option):
    """This functions purpose is to change the customers order."""

    keep_going = True
    while keep_going:
        if option == "n":
            print("Order Confirmed. \n")
            final()
            keep_going = False
        elif option == "y":
            item = input("What item would you like to change? > ").title()
            while item not in (order_out):
                item = input("What item would you like to change? > ").title()
            amount = int(input("How many would you like? > "))
            while amount > 5 or amount < 0:
                try:
                    amount = int(input("How many would you like? Cannot be greater than 5 or less than 0 > "))
                except ValueError:
                    print("Please enter a valid input. ")
            order_out[item] = amount
            for i in order_check:
                x = menu[i]['item']
                if x == item:
                    order_check[i] = amount
            option = input("Would you like to change another item? y/n > ")


def final():
    """This functions purpose is to display the final order to the customer."""

    print("Finalising order.\n")
    print("Order for", name, "> Deliver to", address, "> Contact No.", phone,)
    print('\n'.join("{}: {}".format(k, v) for k, v in order_out.items()))
    total_price = calc(order_check)
    print("Total Cost: $"+str(total_price))


# Main program
greeting()
name = customer_name()
address = address()
phone = phone()
while loop:
    display()
    customer_order = order()  # Gets the customers order
    order_check = check()  # Checks if anything is over the limit
    total_cost = calc(order_check)  # Price calculation
    order_confirm = confirm()
    change(order_confirm)
    cont = input("Would you like to make another order? y/n > ").lower()
    while cont not in ("y", "n"):  # Makes sure that the input is either y or n
        cont = input("Would you like to make another order? y/n > ").lower()
    if cont == "y":  # If you want to make another order, this just wipes the dictionaries from old order
        print("")
        order_check.clear()
        customer_order.clear()
        order_out.clear()
    else:
        loop = False
