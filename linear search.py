# linear search pseudocode
# - create function with two parameters which are an array and value
# - loop through the array and check if the current array element is equal to the value
# - if it is return the index at which the element is found
# - if the value is never found return -1
# time complexity -> O(n) and space complexity -> O(1)
def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linear_search([20,40,30,50,90], 100))