# print("***************WELCOME TO ATM***************")
# pin=int(input("Enter your pin\t"))
# if pin==1234:
#     amount=50000
#     print("1.Withdraw")
#     print("2.Balance Enquiry")
#     option=int(input("Enter your option:\t"))
#     if option==1:
#         new_amount=int(input("Enter the amount to withdraw:\t"))
#         if new_amount>amount:
#             print("Not enough balance")
#         else:
#             rem=amount-new_amount
#             print("Remaining balance is:\t",rem)
#             print("Withdrawn amount is\t",new_amount)
#     elif option==2:
#         print("Your balance is:\t",amount)
#     else:
#         print("Invalid option")
# exit()


# print("***********WELCOME TO DARAZ***********")
# name=input("Enter your name:-\t")
# print("Your name is:-\t",+name)
# amount=int(input("Enter your money amount:-\t"))
# print("Your money before transaction is:-\t")
# print("1.Buy Mobile Phones")
# print("2.Buy Laptops")
# print("3.Buy PC")
# quantity=int(input("Enter the quantity:-"))
# choice=int(input("Enter your choice"))
# if option==1:
#     print("The price of mobile phone is 20000")
#     if amount>20000:
#         rem=(amount-20000)*quantity
#     print("You have successfully purchased your mobile phone and your remaining balance is:",rem)
# else:
#     print("Not enough money to purchase the phone.")
#     elif option==2:
# print("The price of laptop is 40000")
# if amount>40000:
#     rem=(amount-40000)*quantity
#     print("You have successfully purchased your laptop and your remaining balance is:",rem")
# else:
#     print("Not enough money to purchase the laptop.")
#     elif option==3:
# print("The price of PC is 50000")
# if amount>50000:
#     rem=(amount-50000)*quantity
#     print("You have successfully purchased your PC and your remaining balance is:",rem")
# else:
#     print("Not enough money to purchase the PC.")
#     exit()


students_list=['ram,sita']
print("1.Add student")
print("2.Remove student")
print("3.Display students")
print("4.Exit")

option=int(input("Choose an option.\t"))

if option==1:
    a=students_list
    b=input("Enter the names of the students to be added:\t")
    c=a+b
else:
    print()