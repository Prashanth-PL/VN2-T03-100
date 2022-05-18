
# Length of string 


from cgitb import reset


name = "prashanthpl"
length = len(name)
print(length)


name1 = "PRASHANTHPL" 
print(name[0:11])
print(name[:-1])
print(name[:8])
print(name[-10:])


print("************END OF STRING LENGTH****************")

# Count characters in string

a = "Change the life, Life teach new lesson every day. Wake up with new hope, never let you down yours self. You change let others will change."
count1 = a.count("life")
count2 = a.count("you")
count3 = a.count("lesson")
print("The string a contains count of life is : ", count1)
print("The string a contains count of you is :", count2)
print("The string a contains count of you is :", count3)



print("********END OF STRING COUNT*********************")



# String slicing

string = "PRASHANTH"
print(string[:])                              
print(string[1:])                              
print(string[3:])                              
print(string[:1])                             
print(string[:3])                              
print(string[0:3])                             
print(string[2:5])                             
print(string[2:len(string) + 5])               
print(string[:-1])                             
print(string[-1:])                             
print(string[-3:-1])                           
print(string[-1:-3])    






# Length of longest string in python

str1 = "Hai how are you doing"
str2 = "I am doing good. What about you"
str3 = "There is a poor weather condition we can not play"
a=len(str1)
b=len(str2)
c=len(str3)
print(a,b,c)

if (a>b) and (a>c):
    print("str1 is longest  ", a)
elif (b>c) and (b>c):
    print("str2 is longest  ", b)
elif (c>a) and (c>b):
    print("str3 is longest ", c)




# First last chars swapping

string1 = "i am learning python software"
string2 = "Python is easy to learn"
print("String in swapcase is :", string2.swapcase())
print("String in swapcase is :", string1.swapcase())


print("**********END OF SWAPPING****************")


# Replace first occurance character

str1 = "prashanth is playing cricket"
print("Brfore replaing : ", str1)
print("After replacing : ", str1.replace("prashanth","Arjun",1))




print("*******END OF REPLACE********")




# Append chars to string at end


a = "Actually i am intrested in nothing rather than"
print("After appending string is : ", a+ "Python") 


print("**************END OF APPEND******************")


# Substring replacement


str1 = "I am prashanth"
str2 = "I am learning python"

substr= str1.replace(str1, str2)
print("After reaplcaing the string :", substr)


str1 = "I am prashanth"
str2 = "I am learning python"
def substr(str1, str2):
    substr = str1.replace(str1, str2)
    print("Substr : ", substr)

substr(str1, str2)

print("**************************END OF SUBSTRING********************")



# nth index character from string

str1 = "hai how are you doing?"








# First last chars swapping

str1 = "PRSHANTHPL"
start=str1 [0] 
end=str1 [-1]
swapped=end+str1[1:-1]+start
print(swapped)

# Upper lower case of a string

string1 = "i am LearNing pyTHon"
print("String1 in upper case ", string1.upper())
print("String1 in lower case  ", string1.lower())

# Sort unique words alphanumerically


str1 = "Usain bolt completed 100meter track in 9.58 seconds "

print("alphanumerically is: ", str1.alphanumeric())













