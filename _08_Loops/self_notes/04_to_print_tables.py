# Write a program to print table of a number (acceplted from user ) in the following format
#  like: input number is 7, so expected output is 

#  7 * 1 = 7
#  7 * 2 = 14 and so on





num = int(input("Enter a number : "))
for i in range (1, 11):
    print(str(num) +  " X "  + str(i) +  " = "  + str(i*num) ) 
    # print(f"{num}X{i}={num*i}")