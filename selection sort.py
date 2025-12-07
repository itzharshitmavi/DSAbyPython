# in case of selection  sort we repeatedly find the minimum element and move it to sorted part of array to make unsorted part sorted
# time complexity : O(n^2) and space complexity : O(1)
# when to use?
# when we hace insufficient memory
# easy to implement
# when to avoid
# when time is concern
def Selection_Sort(custom_list):
    for i in range(len(custom_list)):
        min_index = i
        for j in range(i + 1, len(custom_list)):
            if custom_list[min_index] > custom_list[j]:
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    print(custom_list)

clist = [2,4,7,0,9,8,5,]
Selection_Sort(clist)