#Imported things
from menu2 import menu

#functions
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
    #s=[] #order list
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
                    #s.append(n) #adds to order list using the item name
                    if n in z:
                        z[n]+=1
                    else:
                        z[n]=quantity #sends the order and quantiy to a dictionary
            elif item == 0:
                return z
        except ValueError:
            print("Not a valid input.")

t=""

#main program
greeting()
customer=customer_name()
delivery_address=address()
contact_number=phone()
display()
a=order()
print(a)