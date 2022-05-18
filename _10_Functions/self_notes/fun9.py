# Accepts a string and calculate the number of upper-case letters and lower-case letters


def funStr(string1):
    u_case_count = 0
    l_case_count = 0
    for i in string1:
        if i.isupper():
             u_case_count += 1
        else:
            l_case_count += 1

    print("Upper-case letter count is :", u_case_count)
    print("Lower-case letter count is :", l_case_count)
funStr("PraShanThPl")

