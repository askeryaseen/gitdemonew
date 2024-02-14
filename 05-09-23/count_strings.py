s1="abcdABCDE123456@#$%^&*"
lowercase = 0
uppercase = 0
number = 0
special_character = 0

for i in s1:
    if i.islower():
        lowercase+=1
    elif i.isupper():
        uppercase+=1
    elif i.isnumeric():
        number+=1
    else:
        special_character+=1
        
print(lowercase)
print(uppercase)
print(number)
print(special_character)