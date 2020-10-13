def order():
    a=0
    while a != 1:
        try:
            #initial input 
            a=1
            return order
        except ValueError:
            print("Please enter a valid input")

h=order()
print(h)