# Prints each item and its corresponding type from the following list.	












# To sort (ascending and descending) a dictionary by value

def funDict():
    key_value = {}
    key_value[6] = 92
    key_value[2] = 20
    key_value[5] = 36
    key_value[3] = 25
    key_value[1] = 50
    key_value[4] = 65
    print("Keys and values sorted in : alphabetical order by the key : ")
    for i in sorted (key_value) :
        print((i, key_value[i]), end = " ")
def main():
    funDict()
if __name__=="__main__":
    main()


# Add a key to a dictionary

dict = {'key1':"Prashanth", 'key2':"rathviraj"}
print("The original dictionary :", dict)
dict['key3'] = "Arjun"
dict['key4'] = "Mangoes"
dict['key5'] = "Hello"
print("updated dictionary :", dict)



dictionary1 = {'key1':"Prashanth", 'key2':"rathviraj"}
print("The original dictionary :", dict)
dictionary2 = {'key3':"Arjun", 'key4': "Hello"}

a = dictionary1.update(dictionary2)
print("Updated dictionary : ", a)


# Check if a given key already exists in a dictionary.









