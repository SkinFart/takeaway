'''
The purpose of this program is to take a customers order from the takeaway chain Joe Nuts.
William Bigley
21/10/20
Version 1
'''

#  Imported things
from menu2 import menu


#  functions
def greeting():
    print("Welcome to Joe Nuts")


def display():
    for i in menu:
        b=menu[i]
        n=b["item"]
        l=b["price"]
        text="${price}\t{item}".format(item=n, price=l)
        print(text)


def customer_name():
    a=0
    while a != 1:
        try:
            name=input("Enter name: ") #initial input 
            if not name.isalpha(): #checks if name contains only characters
                print("Please enter only alphabetical characters for your name. ")
            else:
                a=1
                return name
        except ValueError:
            print("Please enter a proper name")


def address():
    a=0
    while a != 1:
        try:
            address=input("Enter delivery address: ") #initial input 
            if address =="":
                print("Address cannot be blank. ")
            else:
                a=1
                return address
        except ValueError:
            print("Please enter a proper name")


def phone():
    a=0
    while a != 1:
        try:
            phone_number=int(input("Enter contact number: ")) #initial input 
            a=1
            return phone_number
        except ValueError:
            print("Please enter a valid input")


def order():
    z={} #test dictionary
    t=input("Would you like to make an order? If not please leave blank. ")
    while t != "":
        try:
            item=int(input("Please make a selection 1-12 of the menu (0 to finish order): "))
            if item >=1 and item <=12:
                quantity=int(input("How many: "))
                if quantity > 5:
                    print("Max order limit is 5. ")
                elif quantity == 0:
                    print("Item not added. ")
                else:
                    f='item'+str(item) #creates item search term
                    d=menu[f] #sets the order item to a variable
                    n=d['item'] #pulls item name from dictionary
                    if f in z:
                        z[f]+=quantity
                        order_out[n]+=quantity
                    else:
                        z[f]=quantity #sends to the list used for calc
                        order_out[n]=quantity #sends to the list to display order
                
            elif item == 0:
                return z
        except ValueError:
            print("Not a valid input.")
  
def check():
    for i in customer_order:
        if customer_order[i] > MAX:
            print(customer_order[i],"was over the limit of 5. Put order quanity to 5 for convinience.")
            customer_order[i]=MAX
            print(i,customer_order[i])
    return customer_order

def calc(bruh):
    z = sum([ menu[b]["price"]*bruh[b] for b in bruh.keys() ])
    #print("Price: " + str(z))
    return z

def confirm():
    print('\n'.join("{}: {}".format(k, v) for k, v in order_out.items()))
    print("Total Cost: $"+str(total_cost))
    edit=input("Would you like to edit your order? y/n ").lower()
    while edit not in ("y","n"):
        edit=input("Would you like to edit your order? y/n ").lower()
    if edit == "n":
        print("L")
    elif edit == "y":
        return edit

MAX=5 #constant for order limit for each item
order_out={} #dictionary to display the customers order

#main program
MAX=5 #constant for order limit for each item
order_out={} #dictionary to display the customers order
display() #displays the menu
while True:
    customer_order=order() #gets the customers order
    order_check=check() #checks if anything is over the limit (due to you being able to add item x multiple times and going over limit)
    total_cost=calc(order_check) #price calculation
    order_confirm=confirm()
    
    cont=input("Would you like to make another order? y/n > ").lower()
    while cont not in("y","n"):
        cont=input("Would you like to make another order? y/n > ").lower()
    if cont == "n":
        break