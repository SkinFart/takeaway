'''skin'''

def customer():
    customer_info=[]
    a=0
    while a==0:
        try:
            name=str(input("What is your name: "))
            #if name != str:
            address=input("What is you delivery address: ")
            phone=int(input("What is your contact number: "))
            customer_info.extend((name, address, phone))
            a+=1
        except ValueError:
            print("Please enter a valid input")
    return customer_info
a=customer()
print(a)