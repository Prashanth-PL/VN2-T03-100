#  length of string
#  Snytax :
# len (string_name)

name = "Prashanth P L"
print(name[0])
print(name[4])
print(name[-3])
print(name[6])

print("-------- END OF LENGTH PY--------------")

str1 = 'I am single quote string '
str2 = "I am double quote string"
str3 = ''' I am triple quote string'''
print(" String 1 is :", str1)
print(" String 2 is :", str2)
print(" String 3 is :", str3)

print("--------------------End of program------------------")

#  Forward And Backward Indexing 

name = "PRASHANTH P L"
# name[0] = 'K'                        ====> We can not item assigment 
print(" Forward ")
print(name [0])
print(name[1])
print(name[6])
print(name[5])

print(" Backward ")
print(name[-1])
print(name[-3])
print(name[-6])
print(name[-2])


print("-------------End OF FORWARD AND BACKWARD PY------------")

#  Forward and Backward py

name = "Prashanth P L"
length = len(name)
i = 0
for j in range (1, length + 1):
    print(" Forward is : ", name[i])
    print(" Backward is :", name[-j])
    i = i + 1

print("------------------------- END OF PROGRAM-------------")


#  String slicing

# Syntax :
#  string - name[lower-index/ start-index:
#                upper-index / end-index]

string = "PYTHON"
print(string[:])                               # PYTHON
print(string[1:])                              # YTHON
print(string[3:])                              # HON
print(string[:1])                              # P
print(string[:3])                              # PYT
print(string[0:3])                             #PYT
print(string[2:5])                             #THO
print(string[2:len(string) + 5])               #THON
print(string[:-1])                             # PYTHO
print(string[-1:])                             # N
print(string[-3:-1])                           #HO
print(string[-1:-3])                           #INVALID


print("-----------------END OF SLICING METHOD------------------")


#  Searching Method

string = "i hi hello hai how hai are hai you ?"
string1 = "hello"
print("The string is find at :", string.find ("hai"))
print("The string is find at :", string.find("hello"))
print("The string is find at :", string1.find("how"))
print("The string is find at :", string1.find("hello"))
print("The string is rfind at : ", string.rfind("hai"))
print("The string is start with :", string.startswith("you"))
print("The string is Ends with : ", string1.endswith("lo"))

# Conversion method

string1 = "i am leArNing pyThoN"
string2 = "This is wrost world baby"

print(" String1 in lower cases : ", string1.lower())
print(" String2 in upper cases : ",  string2.upper())
print(" String1 in first char upper case : ", string1.capitalize())
print(" string2 in title : ", string2.title())
print(" String1 in swapcase :", string1.swapcase())
print(" String2 in replace : ", string2.replace("wrost","Good, Handsome, Brave, Cute"))
print(" String1 split is :", string1.split())


print("-------------------END OF THE PROGRAM-----------------")


string1 = "123"
string2 = "hai"
string3 = "hai123"
string4 = "ABD"
string5 = "abcd"
string6 = "  "
print(" isalnum is : ", string1.isalnum())
print(" isalnum is :", string2.isalnum())
print(" isalpha is : ", string2.isalpha())
print(" islanum is : ", string3.isalnum())
print(" isdigit is : ", string1.isdigit())
print(" islower is : ", string4.islower())
print(" isspace is : ", string6.isspace())


print("-------------END OF PROGRAM-----------------------")

