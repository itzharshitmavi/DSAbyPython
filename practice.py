from array import *
# 1. creating array and traverse
my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)
# 2. access individual elements through indexes
print(my_array[0])
print(my_array[2])
# 3. append any value to the array using append() method
my_array.append(6)
print(my_array)
# 4. insert value in an array using insert() method
my_array.insert(0,11)
print(my_array)
# 5. extend array using extend() method
my_array1 = array('i', [10,11,12])
my_array.extend(my_array1)
print(my_array)
# 6.add item from the list into the array using fromlist() method
temp_list = [20,21,22]
my_array.fromlist(temp_list)
print(my_array)
# 7. remove an array element using remove() method
my_array.remove(22)
print(my_array)
# 8. remove last array element using pop() method
my_array.pop()
print(my_array)
# 9. fetch the element through index using index() method
print(my_array.index(20))
# 10. reverse the python array using reverse() method
my_array.reverse()
print(my_array)
# 11. get array buffer info through buffer_info() method
print(my_array.buffer_info())
# 12. check for number of occurrence of an element using count() method
my_array.append(11)
print(my_array)
print(my_array.count(11))
# 13. convert array to string using tostring() method
strng = my_array.tostring()
print(strng)
ints = array('i')
ints.fromstring(strng)
print(ints)
# 14. convert array to a list with same element using tolist() method
# print(my_array.tolist())
# 15. append a string to char array using fromstring() method
# ints = array('i')
# ints.fromstring(strng)
# print(ints)
# 16. slice elements form an array
print(my_array[1:4])
print(my_array[:4])
