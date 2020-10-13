
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
            
g=customer_name()
print(g)
