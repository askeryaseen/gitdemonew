from tkinter import *

root = Tk()
root.title("form using tkinter")
root.geometry("500x300")
root.configure(bg='lightgrey')

enter_info = Label(root,text="please enter your information: ")
enter_info.grid(row=0,column=1, columnspan = 4,padx =5 , pady = 5)

Label(root,text='Name' ,bg ="lightgrey").grid(row=1,column=1)

name = Entry(root , bd=3)
name.grid(row=1,column=2 ,padx=5,pady=5)

Label(root,text='Email' ,bg ="lightgrey").grid(row=3,column=1)
email = Entry(root,bd=3)
email.grid(row=3,column=2,padx=5,pady=5)

Label(root,text="phone_no",bg="lightgrey").grid(row=4,column=1)
phone_no=Entry(root,bd=3)
phone_no.grid(row=4,column=2,padx=5,pady=5)

Label(root,text="Password",bg="lightgrey").grid(row=5,column=1)
password=Entry(root,bd=3)
password.grid(row=5,column=2,padx=5,pady=5)

Label(root,text="Confirm  Password",bg="lightgrey").grid(row=6,column=1)
Confirm_password=Entry(root,bd=3)
Confirm_password.grid(row=6,column=2,padx=5,pady=5) 

# num =Label(text="Enter your name ?",fg= 'blue',bg='red')
# num.grid(row=1,column=1)




root.mainloop()