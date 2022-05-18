#  if.py syntax:

'''
Syntax :
if condition:
    statement
'''
age =int(input("Enter the number"))
if age >=18:
    print( "Person is eligible for vote")


print("*********************************")

a = 20
b = 30
if a <= b:
    print("Correct")
else:
    print("wrong")

print("********************************")


age = int(input("Enter an age : "))
if age <= 18:
    print("The person is teenage ")
if age >18 and age <= 40:
    print("The person is adult")
if age >40 and age <= 60:
    print("The person is in middle age")

print(" --------END OF if CONDITION OR DECISION -------------")



# if-else.py 
'''
syntax:
if condition:
    statements
else condition:
    statements
'''


age = int(input("Enter the age : "))
if age >= 18:
    print( "Person is eligible for vote")

else:
    print("Person not eligible for vote")

print("*********************************")



num = int(input("Enter a number : "))
if num %3 == 0:
    print("This is an if block ")
    print("Number is an odd number ")

else:
    print("This is an else block")
    print("Number is an even number")


print("--------- END OF if-else CONDITION OR DECISION -------")


#  if elif-else condition

'''
synatax:
if condition:
    statement
elif condition:
    statement
elif condition:
    statement
elif condition:
    statement
else condition:
    statement
'''
num = 1122
if 9 < num < 99:
    print("Two digits number")
elif 99 < num < 999:
    print("Three digits number")
elif 999 < num < 9999:
    print("Four digits number")
else:
    print("number is <= 9 or >= 9999")

print("*****************************************")



a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a > b and a > c:
    print("a is big : ", a)
elif b > a and b > c:
    print(" b is big : ", b)
elif c > a and c > b:
    print(" c is big : ", c)
else:
    print(" Two two and three numbers are same ")


print("*************************************")



litter = int(input("Enter how many puppies were born ? "))
if litter <= 5:
    print(" Good Size ")
elif litter == 6 :
    print(" Just Right ")
elif litter == 7 :
    print(" Large Litter ")
else:
    print(" Goodness Me ")


print("--------------END OF if-elif-else CONDITIONS ---------------")
