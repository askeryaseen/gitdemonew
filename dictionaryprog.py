a = {'name':'anu','age':21,'place':'eklm'}
b = {'name':'thomas','age':3,'phn':65987}
c = { }
for i in a:
    for j in b:
        if i==j:
            c[i]=a[i]+b[j]
        if j not in c:
            c[j]=b[j]
    if i not in c:
        c[i]=a[i]
print(c)