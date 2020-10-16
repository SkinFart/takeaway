from menu2 import menu

def display():
    for i in menu:
        b=menu[i]
        m=b["id"]
        n=b["item"]
        l=b["price"]
        text="{id}.\t${price}\t{item}".format(item=n, price=l, id=m)
        print(text)

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
a=0
order_info=[]

display()
a=order()
print(a)

