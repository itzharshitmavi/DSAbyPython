# divide the given array to two parts
# take first element form unsorted array and find its correct position in sorted array
# repeat untill unsorted array is completed
# time complexity : O(n^2) and space complexity : O(1)
# when to use?
# when we have insufficient memory
# easy to implement
# when we have continuous inflow of numbers and we want ot keep them sorted
# when to avoid?
# when time is concern
def Insertion_sort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i-1
        while j >= 0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -= 1
        custom_list[j+1] = key
    print(custom_list)

clist = [2,4,7,0,9,8,5,]
Insertion_sort(clist)