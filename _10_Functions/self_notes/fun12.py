# Function to check whether a string is a palindrome or not




my_list = ["arun", "madam", "malayalam", "pip", "practice", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
print(result)