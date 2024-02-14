a=int(input("enter a number \n"))
if (a%2==0):
    # print(f"{a} is visible by 2")
    if(a%5==0):
        print(f"{a} is divisible by 2 & 5")
    else:
        print(f"{a}is not divisible by 5 but divisible by 2")      
else:
    if (a%5==0):
        print(f"{a} divisible by 5 but not divisble by 2")
    else:
        print(f"{a} is not divisible by 2 & 5")