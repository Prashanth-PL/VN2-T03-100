myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherfict": {'harry': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys()))   #prints the keys of the dictionary Also converting into list of dict
print(myDict.values())      #Prints the values of the dictionary
print(myDict.items())       #prints the (key,value) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish" : "Friend",
    "Prathviraj" : "Friend",
    "harry" : " A Dancer"
}
myDict.update(updateDict)    # updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("harry"))    # Prints values associated with key "harry"
print(myDict["harry"])        #prints value associated with key "harry"

#  The difference between .get and [] syntax in Dictionaries?
print(myDict.get("harry2"))    # Returns None as harry2 is not present in the dictionary
print(myDict["harry2"])        # throws an error as harry2 is not present in the Dictionary