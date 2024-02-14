n=int(input("enter the number  ? "))
sq=n*n
f=0
while n>0:
    d=n%10
    d1=sq%10
    if d!=d1:
        f=1
    sq//=10
    n//=10
if f==0:
    print("yes its automorphic number")
else:
    print("no its not automorphic number")