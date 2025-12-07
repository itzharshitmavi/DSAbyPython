import math
# create bucket and distribute elements of array into buckets
# sort buckets individually
# merge buckets after sorting
# formula for calculating number of buckets = round(sqrt(number of elements))
# eg., list  = 5,3,4,7,2,8,6,9,1
# eg., round(sqrt(9)) = 3 (so three buckets)
# formula for which number goes to which bucket = ceil(value * number of buckets / maxvalue)
# eg., ceil(5*3/9) = ceil(1.6) = 2 (so number 5 goes in 2nd bucket)
# eg., ceil(3*3/9) = ceil(1) = 1 (so number 3 goes in 1st bucket)
# then, sort all buckets using any sorting algorithms
# time complexity is O(n^2) and space complexity is O(n)
# when to use?
# when input is distributed over range
# eg., 1,2,4,5,9,8,7,9 ✔️(uniform difference)       1,2,4,92,94,96 ❌(large difference)
# when to avoid?
# when space is a concern
def Insertion_sort(customlist):
    for i in range(1, len(customlist)):
        key = customlist[i]
        j = i-1
        while j >= 0 and key < customlist[j]:
            customlist[j+1] = customlist[j]
            j -= 1
        customlist[j+1] = key
    return customlist
def Bucket_sort(custom_list):
    number_of_bucket = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    arr = []
    for i in range(number_of_bucket):
        arr.append([])
    for j in custom_list:
        index_b = math.ceil(j*number_of_bucket/max_value)
        arr[index_b-1].append(j)
    for i in range(number_of_bucket):
        arr[i] = Insertion_sort(arr[i])
    k = 0
    for i in range(number_of_bucket):
        for j in range(len(arr[i])):
            custom_list[k] = arr[i][j]
            k += 1
    return custom_list

clist = [2,1,7,6,5,3,4,9,8]
print(Bucket_sort(clist))