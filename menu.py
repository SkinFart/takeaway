import tkinter
from menu2 import menu

def display():
    for i in menu:
        b=menu[i]
        n=b["item"]
        l=b["price"]
        text="${price}\t{item}".format(item=n, price=l)
        print(text)

display()



#top = tkinter.Tk()
# Code to add widgets will go here...

#top.mainloop()