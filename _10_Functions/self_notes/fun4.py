# write a function to find factorial of given number ?

def factorial_iter(n):
    product = 1
    for i in range (n):
        product = product * ( i + 1 )
    return product
n = int(input("Enter the number :"))
fact = factorial_iter(n)
print("The factorial of given number is :", fact)