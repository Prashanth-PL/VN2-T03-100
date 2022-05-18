def funcret(num):   # func inside a function
    if num==0:
        return print
    if num==1:
        return sum
a=funcret(0)
print(a)

