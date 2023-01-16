from array import *

# 1. Create an array and traverse

my_array = array('i',[1,2,3,4,5])

for i in my_array:
    print(i)


#time complexity = O(n)

# 2. Access individual elements through indexes
print('```````2```````')
print(my_array[0])

#3. Append any value to the array using append() method
print('````````3``````')
my_array.append(6)
print(my_array)

#4. Insert value in an array using insert() method
print('````````4``````')
my_array.insert(0,11)
print(my_array)

#5. Extend array using extend() method
print('````````5``````')
my_array1 = array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)

#6. Add items from list into array using fromlist() method
print('````````6``````')
tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)


#7. Remove any array element using remove() method
print('````````7``````')
my_array.remove(11)
print(my_array)
#O(n) time complexity

#8. Remove last array element using pop() method
print('````````8``````')
my_array.pop()
print(my_array)

#9. Fetch any element through its index using index() method
print('````````9``````')
print(my_array.index(21))

#10. Reverse array using reverse() method
print('````````10``````')
my_array.reverse();
print(my_array)

#11. Get array bugger information through buffer_info() method
print('````````11``````')
print(my_array.buffer_info())

#12. Check for number of occurences of an element using count() method
print('````````12``````')
print(my_array.count(11))

#13. Convert array to string using tobytes() method
print('````````13``````')
strTemp = my_array.tobytes()
print(strTemp)

#14. Convert array to list with same elements using tolist() method
# print('````````14``````')
# print(my_array.tolist())

# 15. Slice elements from an array 
print('````````15``````')
print(my_array[1:4])
print(my_array[2:])
