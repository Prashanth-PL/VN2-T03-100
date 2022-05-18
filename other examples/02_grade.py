#  Accept the percentage from the user and display the grade according to the following criteria:

#  below 25 ----D
#  25 to 45 ----C
#  45 to 50 ----B
#  50 to 60 ----B+
#  60 to 80 ----A
#  Above 80 ----A+


marks = int(input("Enter the number : "))
if marks <0 and marks >100:
    print("Enter the valid marks between 0 to 100: ")
else:
    if marks >=60 and marks <=80:
        print("Reasult! \nScored A grade ")

    elif marks >80 and marks <=100:
        print("Result! \nScored A+ grade ")
    
    elif marks >=50 and marks <60:
        print("Result! \nScored B+ grade")

    elif marks >=45 and marks <50:
        print("Result! \nScored B grade ")

    elif marks >=25 and marks <45:
        print("Result! \n Scored C grade")

    else:
        if marks <25:
            print("Result! \n Scored D grade ")



