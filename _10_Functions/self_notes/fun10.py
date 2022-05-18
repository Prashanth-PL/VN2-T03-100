# Take a list and return a new list with unique elements of the first list

def fun_uni_list(list1):
    unquieList = []
    for i in list1:
        if i not in unquieList:
            unquieList.append(i)
    for i in unquieList:
        print(i)
list1 = [12, 20, 63, 20, 7, 36, 82, 7, 36, 56, 92]
print("The unquie list from the list1 is ", end ='')
fun_uni_list(list1)