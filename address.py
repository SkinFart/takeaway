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

h=address()
print(h)