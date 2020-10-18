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
                    if n in z:
                        z[n]+=quantity
                    else:
                        z[n]=quantity #sends the order and quantiy to a dictionary
                
            elif item == 0:
                return z
        except ValueError:
            print("Not a valid input.")
  
def check():
    for i in a:
        if a[i] > MAX:
            print(a[i],"was over the limit of 5. Put order quanity to 5 for convinience.")
            a[i]=MAX
            print(i,a[i])
    return a

def calc():

    return "skin"

t=""
MAX=5

display()
a=order()
print(a)
skin=check()
print(skin)
q=calc()
print(q)