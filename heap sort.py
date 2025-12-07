# step 1: insert data to binary heap tree
# step 2: extract data from binary heap
# it is best suited with array it does not work with linked list
# time complexity -> O(nlogn) and space complexity -> O(1)
def Heapify(custom_list, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n  and custom_list[l] < custom_list[smallest]:
        smallest = l
    if r < n and custom_list[r] < custom_list[smallest]:
        smallest = r
    if smallest != i:
        custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
        Heapify(custom_list, n, smallest)

def Heap_Sort(custom_list):
    n = len(custom_list)
    for i in range(int(n/2)-1, -1, -1):
        Heapify(custom_list, n, i)
    for i in range(n-1, 0 , -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        Heapify(custom_list, i, 0)
    custom_list.reverse()

clist = [2,1,7,6,5,3,4,9,8]
Heap_Sort(clist)
print(clist)
