# what is binary heap?
# A binary heap is a binary tree with following properties. In a binary heap each node can have at most two children.
# - a binary heap is either min heap or max heap. In a min binary heap, the key at root must be minimum among all keys
# present in binary heap. The same property must be recursively true for all nodes in binary tree.
# - it's a complete tree (all levels are completely filled except possibly the last level and the last level has all keys
# as left as possible). This property of binary heap makes them suitable
# case 1. a value of given node must be less than the value of it's children this case is called minimum heap.
#                               70
#                            /       \
#                         10          20
#                       /  \         /   \
#                     30    40      50   60
#                   /   \
#                 70     80
# case 2. in the case of root is grater than it's children's value this case is called maximun heap
#                               80
#                            /       \
#                         70          60
#                       /  \         /   \
#                     50    40      30    20
#                   /   \
#                 5     10
# why we need a binary heap?
# find the minimum or maximum number among a set of numbers of logN time. And also we want to make sure that inserting additional numbers does not take more than O(logN) time.
# practical use -:
# - Prim's Algorithm
# - Heap sort
# - Priority Queue
# type of binary heap-:
# min heap -> the value of each node is less than or equal to the value of both its children
# max heap -> it is exactly the opposite of min heap that is the value of each node is more than or equal to the value of both its children
# based on these formulas we insert values to array or list in python -:
# 1. left child = cell[2x]
# 2. right child = cell[2x + 1]

class Heap:
    def __init__(self, size):
        self.custom_list = (size+1) * [None]  #---------------->O(1)
        self.heap_size = 0   #---------------->O(1)
        self.max_size = size + 1   #---------------->O(1) (space complexity is O(N))
def peek_of_heap(root_node):
    if not root_node:
        return   #---------------->O(1)
    else:       # (space and time both are O(1))
        return root_node.custom_list[1]   #---------------->O(1)
def size_of_heap(root_node):
    if not root_node:
        return    #---------------->O(1)
    else:     # (space and time both are O(1))
        return root_node.heap_size    #---------------->O(1)
def level_order_traversal(root_node):
    if not root_node:
        return  #---------------->O(1)
    else:  # so -> time complexity is O(N) and space complexity is O(1)
        for i in range(1, root_node.heap_size+1):  #---------------->O(N)
            print(root_node.custom_list[i])  #---------------->O(1)
def heapify_tree_insert(root_node, index, heap_type):
    parent_index = int(index/2)  #---------------->O(1)
    if index <= 1:  #---------------->O(1)
        return
    if heap_type == "Min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]  #---------------->O(1)
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type) #---------------->O(logN)
    elif heap_type == "Max":   # so time and space complexity is O(logN)
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]  #---------------->O(1)
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)  #---------------->O(logN)
def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return "the binary heap is full" #---------------->O(1)
    root_node.custom_list[root_node.heap_size + 1] = node_value #---------------->O(1)
    root_node.heap_size += 1 #---------------->O(1)
    heapify_tree_insert(root_node, root_node.heap_size, heap_type) #---------------->O(logN)
    return "the value is successfully inserted" #---------------->O(1)   so time and space complexity is O(logN)
def heapify_tree_extract(root_node, index, heap_type):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0
    if root_node.heap_size < left_index:
        return
    elif root_node.heap_size == left_index:
        if heap_type == "Max":
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
        else:
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
    else:
        if heap_type == "Min":
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] > root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
        else:
            if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
        heapify_tree_extract(root_node, swap_child, heap_type)
def extract_node(root_node, heap_type):
    if root_node.heap_size == 0: #------------> O(1)
        return
    else:  # so time and space complexity is O(logN)
        extracted_node = root_node.custom_list[1]  #------------> O(1)
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]  #------------> O(1)
        root_node.custom_list[root_node.heap_size] = None  #------------> O(1)
        root_node.heap_size -= 1  #------------> O(1)
        heapify_tree_extract(root_node, 1, heap_type) #------------------> O(logN)
        return extracted_node  #------------> O(1)
def delete_entire_binary_heap(root_node):
    root_node.custom_list = None

new_binary_heap = Heap(5)
print(size_of_heap(new_binary_heap))
print('===================================================================')
insert_node(new_binary_heap, 4, "Max")
insert_node(new_binary_heap, 5, "Max")
insert_node(new_binary_heap, 2, "Max")
insert_node(new_binary_heap, 1, "Max")
level_order_traversal(new_binary_heap)
print('===================================================================')
print(extract_node(new_binary_heap,"max"))
print('======================================================================')
level_order_traversal(new_binary_heap)
print("================================================================")
delete_entire_binary_heap(new_binary_heap)
print('==============================================')
level_order_traversal(new_binary_heap)


# operations                       time complexity          space complexity
# creating                              O(1)                    O(N)
# peek                                 O(1)                     O(1)
# size                                 O(1)                    O(1)
# traversal                             O(N)                   O(1)
# insert                              O(logN)                 O(logN)
# extract                             O(logN)                 O(logN)
# delete entire tree                    O(1)                    O(1)