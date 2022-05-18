# Returning multiple values from a function

# return sum, sum
#   output
#  The sum is :150
#  The substraction is: 50



def sum_sub_fun(n1, n2):
    result1 = n1 + n2
    print("The sum of given number is ", result1)
    
    result2 = n1 - n2
    print("The substraction of given number is ", result2)
        
    
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second Number :"))
sum_sub_fun(n1, n2)


