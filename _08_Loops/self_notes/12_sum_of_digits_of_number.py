#  Write the program to find the sum of digits of a number accepted from user?

Num=int(input("Enter a number:"))
sumn=0
rem=0
while Num>0:
    rem=Num%10
    sumn=sumn+rem
    Num=Num//10
print("sum of given num is:",sumn)
