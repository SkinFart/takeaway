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
    a=0
    order=[]
    while a!=0:
        try:
            item=input("Please make a selection: ")
        except ValueError:
            print("Not a valid input.")


    #if item in menu:
        return("skin")




display()
order()
print(x)
