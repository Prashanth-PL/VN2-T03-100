# Accept the following  from the user and calculate the percentage of class attended?

#  a) Toatal number of working Days
#  b) Total number of days for absent

# After calaculating percentage show that, if the percentage 
# is less than 75, than student will not be able to sit in exam



workingDays = int(input("Enter total number of working days :  "))
absent = int(input("Entetr the number of days absent :  "))

totalpercentage = ((workingDays-absent)/workingDays)*100
print("Total percentage of class attended ", totalpercentage)

if totalpercentage < 75:
    print("Student will not be able to sit in exam ")