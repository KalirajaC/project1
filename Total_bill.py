
# declare the prices of the products
coffee_price=100
vadai_price=100
sanwich_price=200
coak_price=60

#  Declare empty discount
discount=0

# getting the input from the customer 

coffee=int(input("Enter coffee count : "))
vadai=int(input("Enter vadai count : "))
sanwich=int(input("Enter sanwich count : "))
coak=int(input("Enter coak count : "))

# Total value of the items

total=(coffee*coffee_price)+(coak*coak_price)+(sanwich_price*sanwich)+(vadai*vadai_price)
print("Total before add discount : ",total)

# Code for discount
if (coffee>=1 and vadai>=1 and sanwich>=1 and coak>=1) or (sanwich>1 and vadai>2) or (total>=1000):
    discount=(20/100*total)
    total=total-discount
# print the final amount which user have to pay  
print("total discount amount: ",discount)
print("Total paying amount: ",total)
