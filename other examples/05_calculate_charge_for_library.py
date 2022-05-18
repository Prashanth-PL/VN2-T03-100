#  Accept the number of Days from the user and calculate the charge for library according to following 

#  Till five days : Rs 2/Day
#  Six to Ten days : Rs 3/Day
#  11 to 15 days : Rs 4/Day
#  After 15 days : Rs 5/Day


user = int(input("Enter the number of Days "))
if user<0:
    print("Enter the valid number ")
    
if user <=5:
    charge = 2*user
    print("The charge for library Till five days", charge)

elif user >=6 and user <= 10:
    charge = 3*user
    print("The charge for library for Six to Ten days", charge)

elif user >=11 and user <=15:
    charge = 4*user
    print("The charge for library for 11 to 15 days ", charge)

else:
    charge = 5*user
    print("The charge for library after 15 days ", charge)

