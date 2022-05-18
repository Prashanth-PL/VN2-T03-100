#  Multiply all the numbers in a list,set,tuple

from itertools import product


print("************PRODUCT OF LIST*************")

def Mylist(l1):
    result = 1
    for i in l1:
        result = result * i
    return result

l1 = [20, 52, 63, 5]
print(Mylist(l1))
l1 = [5, 5, 5, 5]
print(Mylist(l1))

print("********PRODUCT OF Tuple***************")

def MyTuple(t1):
    result = 1
    for i in t1:
        result = result * i
    return result

t1 = (5, 6, 8)
print(MyTuple(t1))
t1 = (10, 8, 6)
print(MyTuple(t1))



print("*************PRODUCT OF SET*****************")

def MySet(s1):
    result = 1
    for i in s1:
        result = result * i
    return result

s1 = (8, 2, 10)
print(MyTuple(s1))
s1 = (8, 3, 9)
print(MyTuple(s1))




