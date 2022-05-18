# Table of given number 

def tableFun(num):
    for i in range (1, 11):
        print(num, "X", i, "=", num*i)

num = int(input("Enter the number "))
tableFun(num)