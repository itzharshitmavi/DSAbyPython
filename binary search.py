# binary search is faster than linear search
# half of the remaining elements can be eliminated at a time, instead of eliminating them one by one
# binary search only work for sorted arrays
# binary search pseudocode-:
# - create function with two parameters which are a sorted array and a value
# - create two pointers: a left pointer at the start of the array and a right pointer at the end of the array
# - based on left and right pointers calculate middle pointer
# - while middle is not equal to the value and start <= end loop:
#   - if the middle is greater than the value move the right pointer down
#   - if the middle is less than the value move the left pointer up
# - if the value is never found return -1
# time complexity-:
# worst case or average case -> O(logn)
# best case -> O(1)
import math
def binary_search(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end)/2)
    print(start, middle, end)
    while not(array[middle] == value) and start <= end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end)/2)
        print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1

custArray = [8,9,12,15,17,19,20,21,28]
print(binary_search(custArray, 15))
