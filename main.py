#import
import tkinter
from menu2 import menu

#functions
def greeting():
    print("Welcome to Joe Nuts")

def display():
    for i in menu:
        b=menu[i]
        n=b["item"]
        l=b["price"]
        text="${price}\t{item}".format(item=n, price=l)
        print(text)

#main program
greeting()
display()