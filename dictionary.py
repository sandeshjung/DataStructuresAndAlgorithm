#Operations and Built in FUnctions

myDict = {'one': 'uno', 'two':'dos', 'three':'tres', 'four':'cuarto'}

#in operator checks only the keys
print('one' in myDict)
print('uno' in myDict)

# to check values use values() method


#to print all keys and values
for key in myDict:
    print(key, myDict[key]) # time complexity O(1)

# python built in functions
#all() 
myDict1 = {0:True, 1:False}
print(all(myDict1))

#any() -- similar to all() method just if one value is true return value is true

myDict2 = {'e':1, 'a':2, 'o':3, 'i':4, 'u':5}
print(sorted(myDict2))