input_number = int(input("enter number"))
l=2
while (l<input_number):
    if input_number%l ==0:
        print(input_number,"its not prime ")
        break
    l+=1
else:
    print("prime")