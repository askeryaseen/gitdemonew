a = [111,4,22,3,4,5]
for i in range (len(a)):
    for j in range(i,len(a)):
        
            if a[i]>a[j]:
                t=a[j]
                a[j]=a[i]
                a[i]=t
print(a)
                
