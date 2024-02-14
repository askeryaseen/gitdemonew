n = int(input("enter no of rows ? :"))

for i in range(n):
    k=n
    for j in range(i):
      
        print(" ",end = " ")
        k-=1
    for j in range(n-i):
        
        print(k,end = " ")
        k-=1
    print()
    
    
#################################################################################################

for i in range(n):
    
    for j in range(i):
        print(" ", end= " ")
    k=1
    for j in range(n-i):
        print(k, end=" ")
        k+=1
    print()
        