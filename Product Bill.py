print("**************COMPUTER BAZAAR**************")
print("1. Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.Mac(Rs.100000)")

product_name=""
dell_price=0
toshiba_price=0
mac_price=0
quantity=0

question=int(input("Enter the product number:\t"))

if question==1:
    product_name="Dell"
    quantity=int(input("Enter the quantity:\t"))
    dell_price=20000*quantity
elif question==2:
    product_name="Toshiba"
    quantity=int(input("Enter the quantity:\t"))
    toshiba_price=30000*quantity
elif question==3:
    product_name="Mac"
    quantity=int(input("Enter the quantity:\t"))
    mac_price=100000*quantity
else:
    print("Invalid Option")
    exit()

print("Delivery option: 1.Home(Rs:1000) 2.Pickup(Rs:0)")
delivery_price=0
delivery_option=int(input("Enter the delivery option:"))
if delivery_option==1:
    delivery_price=1000

print("Packing Option: 1. Plastic Bag(Rs.10) 2.Bag(Rs.100) 3.Gift Box(Rs.1000)")
packing_price=0
packing_option=int(input("Enter the packing option:"))
if packing_option==1:
    packing_price=10
elif packing_option==2:
    packing_price=100
elif packing_option==3:
    packing_price=1000

total_price=dell_price+toshiba_price+mac_price
tax_amount=0
print("Location 1. KTM(Rs:113%) 2.Lalitpur(Rs:0%) 3.Bhaktapur(Rs:0%)")

location=int(input("Enter the location:\t"))
if location==1:
    tax_amount=total_price*0.13

grand_total=total_price+packing_price+delivery_price+tax_amount

print("++++++++++++INVOICE++++++++++++")
print("Product Name:",product_name)
print("Quantity:",quantity)
print("Total Price:",total_price)
print("Delivery Price:",delivery_price)
print("Packing Price:",packing_price)
print("Tax Amount:",tax_amount)
print("Grand Total:",grand_total)
print("***********THANK YOU FOR YOUR VISIT***********")


print("==============Bhatbhateni Supermarket Store=============")
print("What Would You Like To Buy", end='?')
print("1.Coke 2.25 Ltr (Rs.300) 2.Fanta 2.25 Ltr (Rs.250) 3.Sprite 2.25 Ltr (Rs.275) 4.Mountain Dew 2.25 Ltr (Rs.280)")

product_name=""
coke_price=0
fanta_price=0
sprite_price=0
mountain_dew_price=0
quantity=0

choose=int(input("Choose the cold drink you want to drink"))

if choose==1:
    cold_drink_name="Coke"
    quantity=int(input("Enter the quantity:\t"))
    coke_price=300
elif choose==2:
    cold_drink_name="Fanta"
    quantity=int(input("Enter the quantity:\t"))
    fanta_price=250
elif choose==3:
    cold_drink_name="Sprite"
    quantity=int(input("Enter the quantity:\t"))
    sprite_price=275
elif choose==4:
    cold_drink_name="Mountain Dew"
    quantity=int(input("Enter the quantity:\t"))
    mountain_dew_price=280
else:
    print("We dont have other drinks at the moment.")
    exit()