a = {'apple':'red','banana':'yellow',1:3}
b = {'apple':'euorope','orange':'green',1:6}
c={}

for i in a:
    for j in b:
        if i==j:
            print(i)
    
            c[i]=a[i]+b[j]
        
        else:
            
            
print(c)
    
    
        