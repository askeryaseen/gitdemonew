n = int((input("enter no of rows ? :")))
k = 0
for i in range(n):
    
    for j in range(i+1):
        
        print(k ,end=" ")
    k+=2    
    print()
        
        ####################### reverse #####################
        
k = 0
for i in range(n):
    for j in range(n-i):
        print(k, end =" ")
    k+=2
    print()