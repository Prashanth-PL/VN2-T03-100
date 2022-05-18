#  A Company decided to give bonus to employee according to following criteria:

# Time period of Service      Bonus

#  More than 10 years          10%
#  >= 6 and  <= 10              8%
#  less than 6 years            5%

# Ask user for their salary and years of service  and print the net bonus amount.


salary = int(input("Enter the salary: "))
service = int(input("Enter the years of service: "))
if service >10:
    netbonus = 0.1*salary
    print("Netbonus of employee serviced more than 10years ", netbonus )

elif service >=6 and service <=10:
    netbonus = 0.08*salary
    print("Netbonus of employee serviced in between 6 to 10 years ", netbonus)

else:
    if service <6:
        netbonus = 0.05*salary
        print("Netbonus of employee seviced below 6 years ", netbonus)   


        

