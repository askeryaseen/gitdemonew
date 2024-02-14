# rows = int(input("enter number of rows ? "))
# m = 1
# for i in range(1,rows+1):
#     for j in range(i):
#         print(m, end = " ")
#         m += 1
#     print()
    
# reverse/////////////

rows = int(input("enter number of rows ? "))
m = 1
for i in range(rows,0,-1):
    for j in range(i):
        print(m , end = " ")
        m += 1
    print()
        