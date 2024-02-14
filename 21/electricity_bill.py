unit = int(input("enter number of units used : ?"))
#350
# category = (unit/100)
# if (unit/100)<=1:
#     print("no charge")
# elif category<=2:
#     bill = (unit-100)*5
#     print(f"bill amount is {bill}")
# else:
#     bill = (unit-200) *10
#     print(f" billamount is {bill}")
if unit <= 100:
    print("no charge ")
if  unit>100 and unit<=200:
    bill= (unit-100)*5
    print(f"bill amount is {bill} ") 
    
if unit >200:
    bill_1=  100 *5
    bill_2 = (unit-200)*10
    total_bill = bill_1 + bill_2
    print(f"bill amount is {total_bill} ")
    
