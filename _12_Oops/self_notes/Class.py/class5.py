class Employee:
    def __init__(self, emp_id, name, email_id, salary):
        self.emp_id = emp_id
        self.name = name
        self.email_id = email_id
        self.salary = salary


    def emp_info(self):
        print("Employee Details are ", self.emp_id, self.name, self.email_id, self.salary)


prashanth = Employee(100,"Prashanth PL", "prashanthpl123@gmail.com", 20000 )
a = prashanth.emp_info()
# print(a)




