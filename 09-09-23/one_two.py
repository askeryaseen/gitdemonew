n = int(input("enter no of rows ? :"))
for i in range(n+1):
    for j in range(i):
        if i%2 == 0:
            print("2" ,end = " ")
        
        else:
            print("1" , end =" " )
    print()