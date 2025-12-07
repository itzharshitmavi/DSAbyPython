# bubble sort is also referred as sinking sort
# we repeatedly compare each pair of adjacent items and swap them if they are in the wrong order
# time complexity : O(n^2) and space complexity : O(1)
# when to use?
# when the input is already stored
# space is concern
# easy to implement
# when to avoid?
# average time complexity is poor
def Bubble_Sort(custom_list):
    for i in range(len(custom_list) -1):
        for j in range (len(custom_list) - i - 1):
            if custom_list[j] > custom_list[j + 1]:
                custom_list[j] , custom_list[j + 1] = custom_list[j + 1], custom_list[j]
    print(custom_list)
clist = [2,4,7,0,9,8,5,]
Bubble_Sort(clist)
