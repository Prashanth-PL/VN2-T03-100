class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiver"
    level = 0

class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer
print(p.level)