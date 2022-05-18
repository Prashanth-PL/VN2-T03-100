#  Sum of all the numbers in a list set tuple

print("************SUM OF LIST*************")

l1 = [20, 5, 36, 85]
def sumList():
    TotalSum = sum(l1)
    return TotalSum
print(sumList())

print("********SUM OF Tuple***************")

t1 = (25, 50, 75, 100)
def sumTuple():
    TotalSum = sum(t1)
    return TotalSum
print(sumTuple())

print("*************SUM OF SET*****************")

s1 = {50, 82, 63, 45}
def sumSet():
    ToatalSum = sum(s1)
    return ToatalSum
print(sumSet())
