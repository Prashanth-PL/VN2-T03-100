#  Write a program to print numbers from 1 to 20 except multiple of 2 & 3


for i in range(1, 21):
    if i *2 and i *3:
        continue
    print(i)