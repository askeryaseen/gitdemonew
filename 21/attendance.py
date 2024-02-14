class_attended = int(input("enter the number of classes attended "))
total_class = int(input("total number of classes "))
attendance_percentage = (class_attended/total_class)*100
if attendance_percentage < 75:
    medical_excuse = input("do you have any medical excuse ? yes or no  ")
    if medical_excuse =="yes":
        print(f"you're allowed to attend exam " )
    else:
        print("you're not allowed to attend exam ")
else:
    print("you're allowed to write exam ")
        