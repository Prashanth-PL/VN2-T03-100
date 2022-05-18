# python program to check Armstrong Number 
# ex: 153 = 1*1*1+5*5*5+3*3*3 //153 is an armstrong number.


class Armstrong:

    def __init__(self, num):
        self.num = num

    def isArmstr(self):
        num1 = self.num
        res = 0
        
        while (num1 != 0):
            remainder = num1 % 10
            res += remainder **3
            num1 //= 10
        if self.num ==res :
            print("Is Armstrong ", self.num)
        else:
            print("Is not Armstrong", self.num)

if __name__ == "__main__":
    num = 520
    check_Armstrong = Armstrong(num)
    check_Armstrong.isArmstr()

    num = 153
    check_Armstrong = Armstrong(num)
    check_Armstrong.isArmstr()