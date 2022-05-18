#  Roman number to interger 
#  Symbol         Value
#    I             1
#    V             5
#    X             10
#    L             50
#    C             100
#    D             500
#    M             1000

# Example 1 :
# input : num = "III"
# outpur: 3

# Example 2 :
# input : num = "LVIII"
# output: 58


class Roman_num:
    def roman_int(self, a):
        value = {'I' : 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        int_value = 0
        for i in range (len(a)):
            if i > 0 and value [a[i]] > value[a[i - 1]]:
                int_value += value[a[i]] - 2 * value[a[i-1]]
            else:
                int_value += value[a[i]]
        return int_value
print(Roman_num().roman_int('IV'))
print(Roman_num().roman_int('ML'))
print(Roman_num().roman_int('X'))
print(Roman_num().roman_int('VI'))


