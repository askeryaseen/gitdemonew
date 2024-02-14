# height = int(input())
# for row in range(1,height+1):
#     print(" " * (height-row),"*" * row)
    
    
rows = int(input("enter number of rows"))

for row in range(1,rows+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
     
    
    