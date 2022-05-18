#  a) write a program to print the following pattern.

#  * * * * 
#  * * * 
#  * * 
#  *



n = 4

for i in range(n, 0, -1):
    for j in range(0, i):
        print("* ", end=' ')
    print("\n")
