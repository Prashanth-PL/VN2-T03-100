#  syntax:
#  list name = [data1, data2, data3, data4,....,datan]
#  list name = [ ]

list1 = [101, 3.14, "Hello", " ", 'Prashanth']
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

# List creation access py

list1 = [10, "Hi", 3.14, "Hello"]
# list1 = [100]                               # We can replace the value of zero index from 10 to 100
print(" Forward Indexing")
print("list1 [0] : ", list1[0])
print("list1[1] : ", list1[1])
print("list1[3] : ", list1[3])

print("Backward Indexing")
print("list[-1] : ", list1[-1])
print("list[-3] : ", list1[-3])

#  List access by using loop py

# list1 = [10, 5, 6, "Hello", "apple"]
# l1 = len[list1]
# print("length = ", l1)
# i = 0
# for j in range(1, l1+1):
#     print("Forward : [", i , "] : " , list1(i))
#     print("Backward :[", -j, "] : ", list1[-j])


#  List string py

'''
syntax:
list_name[lower_index/start_index : upper_index/stop index]

'''

list1 = [9, 6, 5, 8, 1, 3, 7, 4]
print(list1)
print(list1[:2])
print(list1[:5])