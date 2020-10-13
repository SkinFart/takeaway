'''This is an input function for the customers information'''

def customer(): #Defining the function
    customer_info=[]
    a=0
    while a==0:
        try:
            name=str(input("What is your name: "))
            address=input("What is you delivery address: ")
            phone=int(input("What is your contact number (no spaces): "))
            customer_info.extend((name, address, phone))
            a+=1
        except ValueError:
            print("Please enter a valid input")
    return customer_info
a=customer()
print(a)