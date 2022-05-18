# check given word is palindrome or not


l1 = ["word", "eye", "level", "wow", "abhishek", "nayana"]
result = list(filter(lambda x: (x == "".join(reversed(x))), l1))
print(result)


word = input("Enter the character :")
if word == word[::-1]:
    print("The string is Palindrome")
else:
    print("Not palindrome")


def palindrome(s):
    return s==s[::-1]
s ="rotator"
res = palindrome(s)
if res:
    print("Its Polindrome")
else:
    print("Its not Plindrome")



# print even and odd numbers


def function1(num):
    if num %2 ==0:
        print("The number is even ")
    else:
        print("The number is Odd ")
function1(5)

print("*******************************************")


num1 = int(input("Enter a number :"))
if num1 %2 == 0:
    print("The number is even ")
else:
    print("The number is Odd ")


# print prime numbers


def primeNumber(num2):
    num2 = int(input("Enter a number :"))
    if num2>1:
        for i in range(1, num2):
            if  num2 %i ==0:
                return False
            else:
                return True
        
        else:
            print("Invalid number ")
print(primeNumber(100))


print("*******************************************")


p = int(input("Enter a number : "))
if p > 1:
    for i in range (2, p):
        if p %i == 0:
            print("Entered Number is not Prime")
        else:
            print("The Entered Number is Prime ")
else:
    print("Input Valid Numbers ")


print("**********************************************")


# factorial of given number

def factorial_iter(n):
    product = 1
    for i in range (n):
        product = product * ( i + 1 )
    return product
factorial_iter(5)


print("****************************************************")

fact = int(input("Enter a number :"))
factorial = 1
if fact <0 :
    print("Invalid")
elif fact ==0:
    print("factorial is 1")
else:
    for i in range (1, fact+1):
        factorial = fact * i
    print("Factorial is :", factorial)



