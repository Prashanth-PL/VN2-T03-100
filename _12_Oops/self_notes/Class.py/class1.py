# python program to check leap year
#  ex: 2000 is a leap year


class Leapcheck:
    def check_Leap_or_Not(self, n):
        if n % 4 ==0 and n % 100 != 0:
            return 1
        elif n % 400 == 0:
            return 1
print("Enter the year : ", end = '')
n = int(input()) 

year = Leapcheck()
a = year.check_Leap_or_Not(n)
if a == 1:
    print("Leap year")
else:
    print("Not a Leap Year")

