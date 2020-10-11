import tkinter

menu={
    "item1": {
        "item": "Brown Shake" ,
        "price": 3.50
    },
    "item2": {
        "item": "Black Shake" ,
        "price": 2
    },
    "item3": {
        "item": "Blue Shake" ,
        "price": 3
    },
    "item4": {
        "item": "Red Shake" ,
        "price": 2.50
    },
    "item5": {
        "item": "Yellow Shake" ,
        "price": 2.50
    },
}
for i in menu:
    b=menu[i]
    #print(menu[i])
    print(b["item"])


top = tkinter.Tk()
# Code to add widgets will go here...

top.mainloop()

a=menu["item4"]
#print(a)