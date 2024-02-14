# rows = int(input("enter number of rows ? "))

# for i in range(1,rows+1):
#     m=1
#     for j in range(i):
#         print(m, end = " ")
#         m += 1
#     print()
    
    # REVERSE
rows = int(input("enter number of rows ? "))  
for i in range(rows,0,-1):
    m=1
    for j in range(i):
        print(m, end = " ")
        m += 1
    print()   