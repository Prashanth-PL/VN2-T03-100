myDict = {
    "Panka": "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options are", myDict.keys())      # myDict.keys is a function returns a list containing dictionary's keys
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))