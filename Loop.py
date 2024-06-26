# WAP to print 10 to 1 using loop.
# x=10
# while x>=1:
#     print(x)
#     x-=1

# WAP to print total even number between 1 to 100.
# x=0
# while x<=100:
#     print(x)
#     x=x+2

# WAP to print your name 10 times.
# x=1
# while x<=10:
#     print("I am Natsu Dragneel")
#     x+=1

students=[]

num=int(input("Enter the number of students:"))
x=1
while x<=num:
    name=input("Enter the name of the student:")
    students.append(name)
    x+=1

a=0
while a<len(students):
    print(students[a])
    a+=1