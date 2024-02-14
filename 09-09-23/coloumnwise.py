n = int(input("enter no of rows ? :"))

for i in range(n):
    k=5
    for j in range(i+1):
        print(k,end=" ")
        k-=1
    print()
    
    
#########################################################################
for i in range(n+1):
    k=1
    for j in range(i):
        print(k ,end =" ")
        k+=1
    print()
        
####################################reverse###############################################
for i in range(n+1):
    k=1
    for j in range(n-i):
        print(k , end = " ")
        k+=1
    print()
        
          