a="recover"
d={}

for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for i in d:
    if d[i]==1:
        print(i,d[i])