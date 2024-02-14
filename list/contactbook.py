contacts={}
while(True):
   
    choice = int(input('''      
                                1.add contact
                                2.view
                                3.delete a contact
                                4.update
                                5 exit\n '''))

    if choice == 1:
        sub = {}
        name = input("enter name ?")
        email = input("email ? ")
        phone = int(input("phone ? "))
        sub['name'] = name
        sub['email'] = email
        sub['phone'] = phone
        contacts[name]=sub
       
        print(contacts)
              
    elif choice == 2:
        print(contacts)
        
    
    elif choice ==3:
        user = input("enter name to delete ")
        del contacts[user]
        print(contacts)
    
    elif choice == 4:
        name = input('enter the name of the contact you want to update')
        update = int(input(''' 1.name
                            2.email
                            3.ph'''))
        
        if update ==1:
            newname = input("enter the new name ")
            contacts[name]['name']=newname
            nn = contacts.pop(name)
            print(nn)
            contacts[newname] = nn
            print(contacts[newname])