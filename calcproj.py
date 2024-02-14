import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.geometry('500x500')

txt = tk.Text(width=30,height=2)
txt.grid(row=0,column=0,columnspan=10)

def one():
    txt.insert(tk.END,'1')
    
def two():
    txt.insert(tk.END,'2')

def three():
    txt.insert(tk.END,'3')

def four():
    txt.insert(tk.END,'4')
    
def five():
    txt.insert(tk.END,'5')
    
def six():
    txt.insert(tk.END,'6')
    

def seven():
    txt.insert(tk.END,'7')
    
def eight():
    txt.insert(tk.END,'8')
    
def nine():
    txt.insert(tk.END,'9')
    
def add():
    txt.insert(tk.END,'+')
    
def sub():
    txt.insert(tk.END,'-')
    
def mul():
    txt.insert(tk.END,'*')
    
def div():
    txt.insert(tk.END,'/')
    
def equ():
    a=txt.get('1.0',tk.END)
    total = eval(a)
    txt.delete('0.0',tk.END)
    txt.insert(tk.END,total)
    
def clear():
    txt.delete('0.0',tk.END)
    
btn1 = ttk.Button(text='1' ,command = one)
btn1.grid(row=1,column=1)

btn2 = ttk.Button(text='2' ,command = two)
btn2.grid(row=1,column=2)

btn3 = ttk.Button(text='3' ,command = three)
btn3.grid(row=1,column=3)

btn4 = ttk.Button(text='4' ,command = four)
btn4.grid(row=2,column=1)

btn5 = ttk.Button(text='5' ,command = five)
btn5.grid(row=2,column=2)

btn6 = ttk.Button(text='6' ,command = six)
btn6.grid(row=2,column=3)

btn7 = ttk.Button(text='7' ,command = seven)
btn7.grid(row=3,column=1)

btn8 = ttk.Button(text='8' ,command = eight)
btn8.grid(row=3,column=2)

btn9 = ttk.Button(text='9' ,command = nine)
btn9.grid(row=3,column=3)

btnadd = ttk.Button(text='+' ,command = add)
btnadd.grid(row=4,column=1)

btnsub = ttk.Button(text='-' ,command = sub)
btnsub.grid(row=4,column=2)

btnmul = ttk.Button(text='X' ,command = mul)
btnmul.grid(row=4,column=3)

btndiv = ttk.Button(text='/' ,command = div)
btndiv.grid(row=5,column=1)

btnequ = ttk.Button(text='=' ,command = equ)
btnequ.grid(row=5,column=2)

btnclear = ttk.Button(text='C' ,command = clear)
btnclear.grid(row=5,column=3)

window.mainloop()