# an AVL tree is self-balancing Binary Search Tree where the difference between heights of left and right subtrees cannot be more than one for all nodes
#                              n1   ✔
#                           /      \
#                         n2❌      n3 ✔
#                       /              \
#                     n4                n6
#                   /   \
#                 n7     n8
# for n1: height of left subtree = 3
# height of right subtree = 2
# so difference = 1
# it is balanced....
# for n3: height of left subtree = 1
# height of right subtree = 1
# so difference = 0
# so it is balanced....
# for n2: height of left subtree = 2
# height of right subtree = 0
# so difference = 2
# it is not balanced....
# if anytime heights of left and right subtrees differ by more than one, then rebalancing is done to restore AVL property, this process is called rotation
# NOTE-: always take grandchild which has big height
# AVL examples:
#                              n1
#                           /      \
#                         n2         n3
#                       /  \        /   \
#                     n4    n5    n6      n7
#                   /
#                  n8
# AVL trees help us to balance the binary search tree and boost its performance of inserting, deleting , and searching operations
# everytime when a tree disbalanced, AVL tree perform some "rotation" to get tree balanced again
# preorder traversal order ----->>>> root node ----> left subtree -----> right subtree ( time complexity : O(n), space complexity O(n) )
# inorder traversal order ----->>>> left subtree ----> root node ---> right subtree ( time complexity : O(n), space complexity O(n) )
# postorder traversal order ----->>>> left subtree -----> right subtree -----> root node ( time complexity : O(n), space complexity O(n) )
# level order traversal ---->>> first we will stack first level in which we have root node then we will continue to the next node level in which we have right and level children of root node, then it continues to the third level so in third level, after visiting all elements, we are continuing to the fourth level ( time complexity : O(n), space complexity O(n) )
# search ----> searched element less than searched node than it go to the left subtree and if it greater than it fo to the right subtree ( time complexity : O(LogN), space complexity O(LogN) )
# insertion a node :- case 1 -> rotation is not required, case 2 -> rotation is required
# disbalance means that left subtree's height and right subtree's height differ more than one
# case 1: rotation is not required -> when the rotation is not required the insertion is same as in binary search tree
#                         |75|   70
#                            /       \
#                         50          90
#                       /  \         /   \
#                     30    60      80     100
#                   /   \
#                  20    40
# after inserting : as there is no disbalance in this case the added node check the value as in this case it is higher so it goes to right side then it lower so it go to left side and again it is lower then again it will go to the left side
#                                70
#                            /       \
#                         50          90
#                       /  \         /   \
#                     30    60      80     100
#                   /   \          /
#                  20    40       75
# case 2: rotation is required ->
# 1. LL - left left condition: (right rotation is required)
#                                70
#                            /       \
#                         50          90
#                       /  \         /   \
# disbalance no ->    30    60      80     100
#               |    /
#           left   20
#             |   /
#          left  10
# after rotation :
#                               70
#                            /       \
#                         50          90
#                       /  \         /   \
#                     20    60      80     100
#                   /  \
#                  10   30
# algorithm:
# rotate_right(disbalanced_node):
#   new_root = disbalanced_node.leftChild
#   disbalanced_node.leftChild = disbalanecd_node.leftChild.rightChild
#   new_root.rightChild = disbalanced_node
#   update height of disbalanced_node and new_root
#   return new_root
# time complexity: O(1) and space complexity: O(1)
# ---------------------------------------------------------------------------------------
# 2. LR - left right condition: (we have to do first left rotation, then we have to do right rotation)
#                                70
#                            /       \
#                         50          90
#                       /  \         /   \
# disbalance node ->  30    60      80     100
#                 |  /
#           left    20
#                     \     |
#                      25   right
# after left rotation:
#                               70
#                            /       \
#                         50          90
#                       /  \         /   \
#                     30    60      80     100
#                   /
#                  20
#                 /
#               25
# after right rotation:
#                               70
#                            /       \
#                         50          90
#                       /  \         /   \
#                     25    60      80     100
#                   /   \
#                  20    30
# algorithm:
# rotate_left(disbalanced_node):
#   new_root = disbalanced_node.rightChild
#   disbalanced_node.rightChild = disbalanced_node.rightChild.leftChild
#   new_root.leftChild = disbalanced_node
#   update height of disbalanced_node and new_root
#   return new_root
# rotate_right(disbalanced_node):
#   new_root = disbalanced_node.leftChild
#   disbalanced_node.leftChild = disbalanced_node.leftChild.rightChild
#   new_root.rightChild = disbalanced_node
#   update the height of disbalanced_node and new_root
#   return new_root
# time complexity: O(1) and space complexity : O(1)
#--------------------------------------------------------------------------------------
# 3. RR - right right condition: (left rotation is required)
#                                50
#                            /       \
#                         40          60  <- disbalanced node
#                                       \           |
#                                        65         right
#                                          \        |
#                                            70     right
# after left rotation:
#                               70
#                            /       \
#                         40          65
#                                    /   \
#                                  60     70
# algorithm:
# rotate_left(disbalanced_node):
#    new_root = disbalanced_node.rightChild
#    disbalanced_node.rightChild = disbalanced_node.rightChild.leftChild
#    new_root.leftChild = disbalanced_node
#    update height of disbalanced_node and new_root
#    return new_root
# time complexity: O(1) and space complexity : O(1)
#----------------------------------------------------------------------------------------------------
# 4. RL - right left condition: ( we have to do first right rotation then we have to do left rotation)
#                                50
#                            /       \
#                         40          60  <-- disbalanced node
#                                       \
#                                        70
#                                       /
#                                      65
# after right rotation:
#                                50
#                            /       \
#                         40          60
#                                       \
#                                        65
#                                          \
#                                            70
# after left rotation:
#                                50
#                            /       \
#                         40          65
#                                    /   \
#                                   60    70
#
# algorithm:
# rotate_right(disbalanced_node):
#   new_root = disbalanced_node.leftChild
#   disbalanced_node.leftChild = disbalanced_node.leftChild.rightChild
#   new_root.rightChild = disbalanced_node
#   update the height of disbalanced_node and new_root
#   return new_root
# rotate_left(disbalanced_node):
#   new_root = disbalanced_node.rightChild
#   disbalanced_node.rightChild = disbalanced_node.rightChild.leftChild
#   new_root.leftChild = disbalanced_node
#   update height of disbalanced_node and new_root
#   return new_root
# time complexity: O(1) and space complexity : O(1)
#-----------------------------------------------------------------------------------------------------------------
# delete a node from AVL tree has three cases:
# 1. the tree does not exist
# 2. rotation is not required (further cases-:)
# a. the node to be deleted is a leaf node
# b. the node to be deleted has one children
# c. the node to be deleted has two children
# 3. rotation is required (further cases-:)
# a. Left left condition (LL) (if the balance is greater than one and if the balance of the left child of root node is greater than zero)
# b. Left right condition (LR) (if the balance is greater than one and the balance of left child is less than zero)
# c. Right right condition (RR) (if the balance is less than minus one and the right child's balance is less than and equal to zero)
# d. Right left condition (RL) (if the balance is less than minus one and the balance of right child is greater than zero)
import QueuedLinkedList as queue
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

    def preorder_traversal(self, root_node):
        if not root_node:
            return
        print(root_node.data)
        self.preorder_traversal(root_node.leftChild)
        self.preorder_traversal(root_node.rightChild)

    def inorder_traversal(self, root_node):
        if not root_node:
            return
        self.inorder_traversal(root_node.leftChild)
        print(root_node.data)
        self.inorder_traversal(root_node.rightChild)

    def postorder_traversal(self, root_node):
        if not root_node:
            return
        self.postorder_traversal(root_node.leftChild)
        self.postorder_traversal(root_node.rightChild)
        print(root_node.data)

    def levelorder_traversal(self, root_node):
        if not root_node:
            return
        else:
            custom_queue = queue.queue_by_linked_list()
            custom_queue.enqueue(root_node)
            while not (custom_queue.is_empty()):
                root = custom_queue.dequeue()
                print(root.value.data)
                if root.value.leftChild is not None:
                    custom_queue.enqueue(root.value.leftChild)
                if root.value.rightChild is not None:
                    custom_queue.enqueue(root.value.rightChild)

    def search_node(self, root_node, node_value):
        if root_node.data == node_value:
            print("the value is found")
        elif node_value < root_node.data:
            if root_node.leftChild.data == node_value:
                print("the value is found")
            else:
                self.search_node(root_node.leftChild, node_value)
        else:
            if root_node.rightChild.data == node_value:
                print("the value is found")
            else:
                self.search_node(root_node.rightChild, node_value)

    def get_height(self, root_node):
        if not root_node:
            return 0
        return root_node.height

    def right_rotate(self, disbalanced_node):
        new_root = disbalanced_node.leftChild
        disbalanced_node.leftChild = disbalanced_node.leftChild.rightChild
        new_root.rightChild = disbalanced_node
        disbalanced_node.height = 1 + max(self.get_height(disbalanced_node.leftChild), self.get_height(disbalanced_node.rightChild))
        new_root.height = 1 + max(self.get_height(new_root.leftChild), self.get_height(new_root.rightChild))
        return new_root

    def left_rotate(self, disbalanced_node):
        new_root = disbalanced_node.rightChild
        disbalanced_node.rightChild = disbalanced_node.rightChild.leftChild
        new_root.leftChild = disbalanced_node
        disbalanced_node.height = 1 + max(self.get_height(disbalanced_node.leftChild),self.get_height(disbalanced_node.rightChild))
        new_root.height = 1 + max(self.get_height(new_root.leftChild), self.get_height(new_root.rightChild))
        return new_root
    # 1 is added because ths get_height method return the left and right child height but here we are setting the disbalanced height so that's why we need to add parent node as well which is disbalanced node after that we need to set the new_root height with the same way that we need for disbalance over here
    def get_balance(self, root_node):
        if not root_node:
            return 0
        return self.get_height(root_node.leftChild) - self.get_height(root_node.rightChild)

    def insert_node(self, root_node, node_value):
        if not root_node: #______________________________________________> O(1)
            return AVLNode(node_value)
        elif node_value < root_node.data:
            root_node.leftChild = self.insert_node(root_node.leftChild, node_value) #--------> O(logN)
        else:
            root_node.rightChild = self.insert_node(root_node.rightChild, node_value) #--------> O(logN)
        root_node.height = 1 + max(self.get_height(root_node.leftChild), self.get_height(root_node.rightChild))
        balance = self.get_balance(root_node) #------------>O(1)
        if balance > 1 and node_value < root_node.leftChild.data:
            return self.right_rotate(root_node) #------------>O(1)
        if balance > 1 and node_value > root_node.leftChild.data:
            root_node.leftChild = self.left_rotate(root_node.leftChild)
            return self.right_rotate(root_node) #------------>O(1)
        if balance < -1 and node_value > root_node.rightChild.data:
            return self.left_rotate(root_node) #------------>O(1)
        if balance < -1 and node_value < root_node.rightChild.data:
            root_node.rightChild = self.right_rotate(root_node.rightChild) #------------>O(1)
        return root_node

    def get_min_value_node(self, root_node):
        if root_node is None or root_node.leftChild is None:
            return root_node
        return self.get_min_value_node(root_node.leftChild)

    def delete_node(self, root_node, node_value):
        if not root_node: #______________________________>O(1)
            return root_node
        elif node_value < root_node.data:
            root_node.leftChild = self.delete_node(root_node.leftChild, node_value) #--------------->O(logN)
        elif node_value > root_node.data:
            root_node.rightChild = self.delete_node(root_node.rightChild, node_value) #----------->O(logN)
        else:
            if root_node.leftChild is None:
                temp = root_node.rightChild
                root_node = None #----------------------> O(1)
                return temp
            elif root_node.rightChild is None:
                temp = root_node.leftChild #--------------------> O(logN)
                root_node = None
                return temp
            temp = self.get_min_value_node(root_node.rightChild) #--------> O(logN)
            root_node.data = temp.data
            root_node.rightChild = self.delete_node(root_node.rightChild, temp.data)
        root_node.height = 1 + max(self.get_height(root_node.leftChild), self.get_height(root_node.rightChild))
        balance = self.get_balance(root_node)
        if balance > 1 and self.get_balance(root_node.leftChild) >= 0:
            return self.right_rotate(root_node)  #---------------> O(1)
        if balance < -1 and self.get_balance(root_node.rightChild) <= 0:
            return self.left_rotate(root_node)  #---------------> O(1)
        if balance > 1 and self.get_balance(root_node.leftChild) < 0:
            root_node.leftChild = self.left_rotate(root_node.leftChild)
            return self.right_rotate(root_node)  #---------------> O(1)
        if balance < -1 and self.get_balance(root_node.rightChild) > 0:
            root_node.rightChild = self.right_rotate(root_node.rightChild)
            return self.left_rotate(root_node)  #---------------> O(1)
        return root_node

    def delete_entire_AVL(self, root_node):
        root_node.data = None #----------->O(1)
        root_node.leftChild = None #---------------> O(1)
        root_node.rightChild = None #----------->O(1)
        return "AVL tree has been successfully deleted"

new_AVL = AVLNode(4)
new_AVL = new_AVL.insert_node(new_AVL, 10)
new_AVL = new_AVL.insert_node(new_AVL, 15)
new_AVL = new_AVL.insert_node(new_AVL, 20)
new_AVL.levelorder_traversal(new_AVL)
print(new_AVL.delete_entire_AVL(new_AVL))

# operations                       time complexity          space complexity
# creating                              O(1)                    O(1)
# insert                                O(logN)                 O(logN)
# traverse                              O(N)                    O(N)
# search                                O(logN)                 O(logN)
# delete                                O(logN)                 O(logN)
# delete entire tree                    O(1)                    O(1)

# operations                            BST                     AVL
# creating                              O(1)                    O(1)
# insert                                O(N)                   O(logN)
# traverse                              O(N)                    O(N)
# search                                O(N)                   O(logN)
# delete                                O(N)                   O(logN)
# delete entire tree                    O(1)                    O(1)


