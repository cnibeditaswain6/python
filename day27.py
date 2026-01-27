# WAP to find the greatest of 3 numbers entered by the user.

a = int(input("Enter the Number(a) : "))
b = int(input("Enter the Number(b) : "))
c = int(input("Enter the Number(c) : "))

if(a > b and a > c ):
    print("Greatest Number is a")
elif(b > c):
    print("Greatest Number is b")
else:
    print("Greatest Number is c")
