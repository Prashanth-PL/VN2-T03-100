# Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers) ?


sum_even = 0
sum_odd = 0

for i in range(12, 37):
    if(i %2==0):
        sum_even = sum_even + i
else:
        sum_odd = sum_odd + i
print("Even sum is: ", sum_even)
print("Odd sum is : ", sum_odd)



    

