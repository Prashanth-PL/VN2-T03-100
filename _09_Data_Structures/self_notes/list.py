# Sum of elements


a = [2, 4, 56, 7]
print("The sum of elements in the list is ", (a[0] + a[1] + a[2] + a[3]))


# Mulitply of elements

b = [3, 5, 9, 7]
print("The product of elements in the list is ", (b[0] * b[1] * b[2] * b[3]))


# Largest number from list

list1 = [25, 65, 20, 725, 500]

list1.sort()
print("Largest  number from list1 is : ", list1[-1])


# Smallest number from list

l1 = [52, 25, 63, 85, 96]

l1.sort()
print("Smallest number from the l1 is : ", l1[0])

# Remove duplicates


list1 = [2, 6, 5, 9, 6, 4, 2, 5, 6]
print("The original list :", list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("After removing duplicates ; ", list2)

# Check list is empty or not


def empty_list(l1):
    if not l1:
        return True
    else:
        return False

l1 = []
if empty_list(l1):
    print("The list is Empty")
else:
    print("The list is not empty")




a = []
if list (a):
    print("The list is Empty")
else:
    print("The list is not empty")



# Clone or copy


a = [12, 52, 85, 96, 32]
b = a.copy()
print(a, b)





