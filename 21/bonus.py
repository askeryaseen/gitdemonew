salary = int(input("enter you salary "))
service = int(input("enter years of service "))
if service < 6:
    bonus = (5/100)*salary
elif service >=6 and service <=10:
    bonus = (8/100)*salary
else:
    bonus = (10/100)*salary
    
print(bonus)   
    