#  python program to make a simple calculator
# ex: Choice = input("Enter choice (1/2/3/4):")
# 1. add
# 2. sub
# 3. mul
# 4. div



class Calculate:
    def __init__(self, n, m):
        self.n = n
        self.m = m
    def add(self):
        return self.n + self.m
    def sub(self):
        return self.n - self.m
    def mul(self):
        return self.n * self.m
    def div(self):
        return self.n / self.m

n = int(input("Enter a first number :"))
m = int(input("Enter a second number : "))
object1 = Calculate(n, m)
while True:
    def menu():
        a = ('1. Add \n2. Sub\n3. multi\n4. divide')
        print(a)
    menu()
    choice = int(input("Please select one of the following : "))
    if choice == 1:
        print("Result : ", object1.add())
    elif choice == 2:
        print("Result : ", object1.sub())  
    elif choice == 3:
        print("Result : ", object1.mul())
    elif choice == 4:
        print("Result : ", object1.div()) 
    elif choice == 0:
        print("Try one of the following again ")
        break
    else:
        print("Invalid option ")
        break
print()    
    
