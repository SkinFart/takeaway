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
    if edit == "y":
        print("")
    elif edit == "n":
        print("Order will be")
    else:
        print("Invalid Input")


t="" #used for loop
MAX=5 #constant for order limit for each item
order_out={} #dictionary to display the customers order

display() #displays the menu
customer_order=order() #gets the customers order
order_check=check() #checks if anything is over the limit (due to you being able to add item x multiple times and going over limit)
total_cost=calc(order_check) #price calculation
confirm()