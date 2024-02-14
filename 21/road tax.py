cost = int(input("enter the cost of the bike ? "))
if cost <=50000:
    tax = (5/100)*cost 
elif cost>50000 and cost<=100000:
    tax =(10/100)*cost
else:
    tax = (15/100)*cost

print(f" your tax is {tax}")