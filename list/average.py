limit = int(input("enter the limit "))
a = []
for i in range(limit):
    num = int(input('enter the numbers '))
    if num == 0:
        break
    else:
        if num%2==0 and num not in a:
            a.append(num)

if len(a)>0:
    s=sum(a)
    average = s/len(a)
    
print(average)
            