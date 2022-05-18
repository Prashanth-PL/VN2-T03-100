# Using OOPs  -- Class
# Step 1:
class Employee:
    # 1. STATE
    empid = 100  # int(input("Enter empid :"))
    name = 'Madhu Nettem'  # input("Enter name : ")
    sal = 15000  # int(input("Enter sal :"))

    # 2. BEHAVIOR
    def get_einfo(empid, name, sal):
        print("Employee details are ", empid, name, sal)
(Employee.get_einfo(empid, name, sal ))
print("---------Using OOPs-----------")