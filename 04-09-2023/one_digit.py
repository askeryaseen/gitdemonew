rows = int(input("enter number of rows ?"))

for i in range(rows,0,-1):
    for j in range(i):  
        print(rows , end = " ")
    print()
    
rows = int(input("enter number of rows ?"))

for i in range(0,rows+1):
    for j in range(i):  
        print(rows , end = " ")
    print()