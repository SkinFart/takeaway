def phone():
    a=0
    while a != 1:
        try:
            phone_number=int(input("Enter contact number: ")) #initial input 
            a=1
            return phone_number
        except ValueError:
            print("Please enter a valid input")

h=phone()
print(h)