user =input("enter the string : ? ").lower()
vowel = "aeiou"
length = len(user)
c = 0
for i in vowel:
    if i not in user:
        print(i ,"not present so all vowels are not present")
        break
    else:
        c+=1
    
    if c==5:
        print("all vowels are presemt")
        
        
