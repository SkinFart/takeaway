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

#main program
greeting()
customer=customer_name()
delivery_address=address()
contact_number=phone()
display()