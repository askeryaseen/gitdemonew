import tkinter as tk
window =tk.Tk()

num = tk.Label(text="Enter two numbers ?",fg= 'blue',bg='red')
num.grid(row=1,column=1)

num1 = tk.Entry(fg='yellow',bg='black')
num1.grid(row=1,column=2)

num2 = tk.Entry(fg="white",bg="black")
num2.grid(row=2,column=2)

displayresult=tk.Label(text="result" ,width=18)
displayresult.grid(row=4,column=2)


def add():
    value1=num1.get()
    value2=num2.get()
    result=int(value1) + int(value2)
    displayresult.config(text=result)
def sub():
    value1=num1.get()
    value2=num2.get()
    result=int(value1) - int(value2)
    displayresult.config(text=result)

def mul():
    value1=num1.get()
    value2=num2.get()
    result=int(value1) * int(value2)
    displayresult.config(text=result)
    
def div():
    value1=num1.get()
    value2=num2.get()
    result=int(value1) / int(value2)
    displayresult.config(text=result)




btn=tk.Button(text="add",command=add)
btn.grid(row=5,column=1)

btn=tk.Button(text="sub",command=sub)
btn.grid(row=6,column=1)

btn=tk.Button(text='mul',command=mul)
btn.grid(row=7,column=1)

btn=tk.Button(text='div',command=div)
btn.grid(row=8,column=1)

window.configure(bg='cyan')
window.geometry("500x500")

window.mainloop()
