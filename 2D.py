import numpy as np
two_D_array = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(two_D_array)
arr = np.insert(two_D_array, 0,[[1,2,3,4]], axis = 0)  # 1 for column and 0 for row
print(arr)
arry = np.append(two_D_array, [[1,2,3,4]], axis = 0)  # at the end of the array
print(arry)

def access_elements(array, row_index, column_index):
    if row_index >= len(array) or column_index >= len(array[0]):
        print('incorrect index')
    else:
        print(arry[row_index][column_index])
access_elements(two_D_array,1,2)

def traverse_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
traverse_array(two_D_array)

def search_element(arr, ele):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == ele:
                return 'the value is located at index ' + str(i) +" "+ str(j)
    return 'the element is not found'
print(search_element(two_D_array,14))

new_TDA = np.delete(two_D_array,0, axis = 1)
print(new_TDA)

# operations                       time complexity          space complexity
# creating an empty array               O(1)                    O(mn)
# inserting a column/row in an array    O(mn)/O(n)              O(1)
# traversing a given array              O(mn)                   O(1)
# accessing a given cell                O(1)                    O(1)
# searching a given value               O(mn)                   O(1)
# deleting a given value                O(mn)/O(1)              O(1)

# when to use?
# 1. to store multiple variables of same data type
# 2. random access
# when to avoid?
# 1. same data type elements
# 2. reserve memory
