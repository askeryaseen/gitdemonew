# rows = int(input("enter no of rows : ?"))
# for i in range (1,rows+1):
#     for j in range(i):
#         print(" * " , end = " ")
#     print()

# REVERSE

rows = int(input("enter number of rows ?"))

for i in range(rows,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()
