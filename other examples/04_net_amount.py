#  Accept the marked price from the user and calculate thre net amount as (Market Price - Discount) to pay according to following criteria
#  Marked Price                         Discount

#  > 10000                                20%
#  > 7000 and <= 10000                    15%
#  <= 7000                                10%



markedPrice = int(input("Enter the price  "))

if markedPrice >10000:
    netamount = (markedPrice-(0.2*markedPrice))
    print("Net Amount to pay ", netamount)

elif markedPrice >7000 and markedPrice <=10000:
    netamount = (markedPrice-(0.15*markedPrice))
    print("Net Amount to pay ", netamount)

else:
    if markedPrice <=7000:
        netamount = (markedPrice-(0.1*markedPrice))
        print("Net Amount to pay ", netamount)

