class Student:

    # STATE

    def __init__(self, roll_no, name, branch, section):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch
        self.section = section

        # BEHAVIOUR

    
    def std_info(self):
        print("Student information is :", self.roll_no, self.name, self.branch, self.section)

# OBJECT CREATION

arjun = Student(20, "Arjun", "Science", "A")
raju = Student(23, "Raju", "Commerce", "C")
preethi = Student(52, "Preethi", "Arts", "B")
a = arjun.std_info()
b = raju.std_info()
c = preethi.std_info()
# print(a)
# print(b)
# print(c)