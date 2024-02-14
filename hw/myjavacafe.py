print("HEY welcome to my java cafe ! ")
item = input("what item do you want to order ? ")
price = int(input("price of the ordered item ? "))
overnight = input("overnight delivery ? yes or no ?")
bill = 0
shipping = 0

if price<10 :
    shipping = 2
    if overnight == "yes":
        print("total" ,price + shipping + 5,"$")
    else:
        print( "total" ,price + shipping,"$")
        
elif price>=10:
    shipping = 3
    if overnight == "yes":
        print("total" ,price + shipping + 5,"$")
    else:
        print( "total" ,price + shipping,"$")
    