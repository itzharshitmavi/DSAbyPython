# merge sort is divide and conquer algorithm
# divide the input array in two halves, and we keep halving recursively until they become too small that cannot be broken futher
# merge halves by sorting them
# time complexity -> O(nlogn) and space complexity -> O(n)
# when to use?
# when you need stable sort
# when average expected time is O(nlogn)
# when to avoid?
# when space is concern
def Merge(custom_list, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = custom_list[l+i]
    for j in range(0, n2):
        R[j] = custom_list[m+1+j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            custom_list[k] = L[i]
            i += 1
        else:
            custom_list[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        custom_list[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        custom_list[k] = R[j]
        j += 1
        k += 1
# here, -:
# l -> first index of list which is the left index
# m -> the middle index of the list
# r -> last index of list which is the right index
# n1 -> number of elements in first subarray
# n2 -> number of elements in second subarray
# L and R -> two temporary arrays

def Merge_Sort(custom_list, l, r):
    if l < r:
        m = (l + (r - 1))//2
        Merge_Sort(custom_list, l, m)
        Merge_Sort(custom_list, m+1, r)
        Merge(custom_list, l, m, r)
    return custom_list

cList = [2,1,7,6,5,7,4,9,8]
print(Merge_Sort(cList, 0, 8))
