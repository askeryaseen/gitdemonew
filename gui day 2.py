import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
txt1=tk.Text()
txt1.grid(row=0,coloumn=0)
def display():
    s=txt1.get()
    
bt1=ttk.Button(text="show",command=display)
btn1.grid(row=3,column=1)
    
window.geometry('500x500')
window.mainloop()


