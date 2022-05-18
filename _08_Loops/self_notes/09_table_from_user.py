# Write a program to print table of a number accepted from user?



num = int(input("Enter a number : "))

for i in range(1, 21):
    print(str(num) + "X" + str(i) + "=" + str(i*num))
