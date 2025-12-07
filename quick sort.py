# quick sort is a divide and conquer algorithm
# find pivot number and make sure smaller numbers located at the left of pivot and bigger
# number are located at the left of pivot
# unlike merge sort extra space is not required
# time complexity -> O(nlogn) and space complexity -> O(n)
# when to use?
# when average expected time is O(nlogn)
# when to avoid
# when space is concern
# when you need stable sort
def Partition(custom_list, low, high):
    i = low - 1
    pivot = custom_list[high]
    for j in range(low, high):
        if custom_list[j] <= pivot:
            i += 1
            custom_list[i], custom_list[j] = custom_list[j], custom_list[i]
    custom_list[i + 1], custom_list[high] = custom_list[high], custom_list[i + 1]
    return (i + 1)
def Quick_Short(custom_list, low, high):
    if low < high:
        pi = Partition(custom_list, low, high)
        Quick_Short(custom_list, low, pi - 1)
        Quick_Short(custom_list, pi + 1, high)

clist = [2,1,7,6,5,3,4,9,8]
Quick_Short(clist, 0, 8)
print(clist)
