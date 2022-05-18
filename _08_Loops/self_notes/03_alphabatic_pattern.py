#  Write a program to print the following pattern

#  A 
#  B C
#  D E F 
#  G H I J
#  K L M N O




ascii_number = 65
rows = 6

for i in range(rows):
    for j in range(1, i + 1):
        a = chr(ascii_number)
        print(a, end=' ')
        ascii_number += 1
    print('')