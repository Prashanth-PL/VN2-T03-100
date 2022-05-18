def dec1(func1):    #func1 taken as an argument, taken dec1 as an function
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
#@dec1
def who_is_prashanth():
    print("prashanth is a python student")

who_is_prashanth = dec1(who_is_prashanth)
who_is_prashanth()
