class Employee:
    company = "Google"


    def ShowDetails(self):
        print("This is an employee")

class Programmer(Employee):
    languge = "Python"
    company = "Youtube"

    def getLanguge (self):
        print(f"The Languge is {self.languge}")

    def ShowDetails(self):
        print("This is an programmer")

e = Employee()
e.ShowDetails()
p = Programmer()
p.ShowDetails()
print(p.company)
# print(p.company)