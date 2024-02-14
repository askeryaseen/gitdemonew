import tkinter as tk
from tkinter import *
window =tk.Tk()
num1 = tk.Label(text="Enter first number ?",fg= 'blue',bg='red',height=20,width=25)
num1.grid(row=1,column=1)

def hi():
    print('hello')
    value=num.get()
    display.config(text=value)
    print(value)

btn=tk.Button(text="click me",command=hi)
btn.grid(row=2,column=2)

num = tk.Entry(fg='yellow',bg='black')
num.grid(row=3,column=3)

display=tk.Label(text='enter number')
display.grid(row=4,column=4)

window.configure(bg='cyan')
window.geometry("500x500")
window.maxsize(1000,1000)
window.minsize(250,250)

window.mainloop()
