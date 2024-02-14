user_string = input("enter string ? ").lower()
vowels = "aeiou"
c = 0
for i in user_string:
    for j in vowels:
        if i==j:
            c+=1
print(c)