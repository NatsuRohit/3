# num=input ("Enter a number")
# num=int(num)
# print(num)
# if (num%2)==0:
#     print("The given number is even")
# else:
#     print("The given number is odd")


# num=input("Enter a number \t")
# num=int(num)
# print(num)
# if (num%3)==0:
#     print("The number is divisible by 3")
# elif (num%5)==0:
#     print("The number is divisible by 5")
# elif ((num%3) and (num%5))==0:
#     print("The number is divisible by 3 and 5")
# else:
#     print("The number is not divisible by 3 and 5")


# age=input("Enter the age of the person \t")
# age=int(age)
# print(age)
# if age>18 and age<40:
#     print("The person is eligible for voting")
# else:
#     print("The person is not eligible for voting")


# num1=int (input("Enter first subjects marks \t"))
# num2=int (input("Enter second subjects marks \t"))
# num3=int (input("Enter third subjects marks \t"))
# num4=int (input("Enter forth subjects marks \t"))
# num5=int (input("Enter fifth subjects marks \t"))
# percentage=((num1+num2+num3+num4+num5)/500)*100
# print(percentage)
# if percentage>=35 and percentage<45:
#     print("C grade")
# elif percentage>=45 and percentage<60:
#     print("B grade")
# elif percentage>=60 and percentage<75:
#     print("A grade")
# elif percentage>=75 and percentage<=100:
#     print("A+ grade")
# else:
#     print("Fail")


# print("1.Add")
# print("2.Sub")
# print("3.Mul")
# print("4.Div")
# print("5.Mod")

# choice=int(input("Enter a number \t"))

# if choice==1:
#     a=int(input("Enter first number \t"))
#     b=int(input("Enter second number \t"))
#     print(a+b)
# elif choice==2:
#     a=int(input("Enter first number \t"))
#     b=int(input("Enter second number \t"))
#     print(a-b)
# elif choice==3:
#     a=int(input("Enter first number \t"))
#     b=int(input("Enter second number \t"))
#     print(a*b)
# elif choice==4:
#     a=int(input("Enter first number \t"))
#     b=int(input("Enter second number \t"))
#     print(a/b)
# else:
#     a=int(input("Enter first number \t"))
#     b=int(input("Enter second number \t"))
#     print(a%b)


#nested if else

username =input('Enter username:\t')
password=input('Enter password\t')

if username=='admin':
    if password=='admin':
        print('Welcome admin')
    else:
        print('Invalid password')
else:
    print('Invalid Username')