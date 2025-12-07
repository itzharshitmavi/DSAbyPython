# binary trees are the data structure in which each node has at most two children, often referred to as the left and right children
# binary tree cannot have more than 2 nodes, it can have 1 but not more than 2 node
# binary tree is a family of data structure(BST, Heap tree, AVL, red black tree, syntax tree)
# why binary tree?
# binary trees are a prerequisite for more advance trees like BST, AVL, red black trees
# huffman coding problem, heap priority problem and expression praising problem can be solved efficiently using binary trees
# In binary search tree the left is always smaller than the value of the root node, and the right child is always bigger then the root node
# binary tree look like this:   n1      \
#                        /  /      \     \
#                      /  n2         n3   *
#                    *  /    \         \  bigger side
#        smaller side n4     n5        n6
#                     /   \
#                    n7    n8
# traversal of binary search tree:-
# Depth first search
# - preorder traversal = root node ----> left subtree ----> right subtree
# - inorder traversal = left subtree ---> root node ----> right subtree
# - post order traversal = left subtree ---> right subtree ---> root node
# breadth first search
# - level order traversal = reach by level one (root node) to last node by going left and right way continuously
# delete a node from BST has three case:-
# - the node has to be deleted is a leaf node
# - the node has one child
# - the node has two children

import QueuedLinkedList as queue
class binary_search_tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    def insert_node(self, root_node, node_value):
        if root_node.data == None:
            root_node.data = node_value
        elif node_value <= root_node.data:
            if root_node.left_child is None:
                root_node.left_child = binary_search_tree(node_value)
            else:
                self.insert_node(root_node.left_child, node_value)
        else:
            if root_node.right_child is None:
                root_node.right_child = binary_search_tree(node_value)
            else:
                self.insert_node(root_node.right_child, node_value)
        return 'the node has been successfully inserted'
    def preorder_traversal(self, root_node):
        if not root_node:
            return
        print(root_node.data)
        self.preorder_traversal(root_node.left_child)
        self.preorder_traversal(root_node.right_child)
    def inorder_traversal(self, root_node):
        if not root_node:
            return
        self.inorder_traversal(root_node.left_child)
        print(root_node.data)
        self.inorder_traversal(root_node.right_child)
    def postorder_traversal(self, root_node):
        if not root_node:
            return
        self.postorder_traversal(root_node.left_child)
        self.postorder_traversal(root_node.right_child)
        print(root_node.data)
    def levelorder_traversal(self, root_node):
        if not root_node:
            return
        else:
            custom_queue = queue.queue_by_linked_list()
            custom_queue.enqueue(root_node)
            while not(custom_queue.is_empty()):
                root = custom_queue.dequeue()
                print(root.value.data)
                if root.value.left_child is not None:
                    custom_queue.enqueue(root.value.left_child)
                if root.value.right_child is not None:
                    custom_queue.enqueue(root.value.right_child)
    def search_node(self, root_node, node_value):
        if root_node.data == node_value:
            print('the value is found')
        elif node_value < root_node.data:
            if root_node.left_child.data == node_value:
                print('the value is found')
            else:
                self.search_node(root_node.left_child, node_value)
        else:
            if root_node.right_child.data == node_value:
                print('the value is found')
            else:
                 self.search_node(root_node.right_child, node_value)
    def mini_value(self, bst_node):
        current = bst_node
        while (current.left_child is not None):
            current = current.left_child
        return current
    def delete_node(self, root_node, node_value):
        if root_node is None:
            return root_node
        if node_value < root_node.data:
            root_node.left_child = self.delete_node(root_node.left_child, node_value)
        elif node_value > root_node.data:
            root_node.right_child = self.delete_node(root_node.right_child, node_value)
        else:
            # node in which we have only one child or not child
            if root_node.left_child is None:
                temp = root_node.right_child
                root_node = None
                return temp
            if root_node.right_child is None:
                temp = root_node.left_child
                root_node = None
                return temp
            # node in which we have two child
            temp = self.mini_value(root_node.right_child)
            root_node.data = temp.data
            root_node.right_child = self.delete_node(root_node.right_child, temp.data)
        return root_node
    def delete_entire_tree(self, root_node):
        root_node.data = None
        root_node.left_child = None
        root_node.right_child = None
        return 'The BST has been successfully deleted'

new_BST = binary_search_tree(None)
print(new_BST.insert_node(new_BST, 70))
print(new_BST.insert_node(new_BST, 50))
print(new_BST.insert_node(new_BST, 90))
print(new_BST.insert_node(new_BST, 30))
print(new_BST.insert_node(new_BST, 60))
print(new_BST.insert_node(new_BST, 80))
print(new_BST.insert_node(new_BST, 100))
print(new_BST.insert_node(new_BST, 20))
print(new_BST.insert_node(new_BST, 40))
print(new_BST.data)
print('=================================================')
print(new_BST.left_child.data)
print('=================================================')
print(new_BST.right_child.data)
print('=================================================')
new_BST.preorder_traversal(new_BST)
print('=================================================')
new_BST.inorder_traversal(new_BST)
print('=================================================')
new_BST.postorder_traversal(new_BST)
print('=================================================')
new_BST.levelorder_traversal(new_BST)
print('=================================================')
new_BST.search_node(new_BST, 60)
print('=================================================')
new_BST.delete_node(new_BST, 20)
print('=================================================')
new_BST.levelorder_traversal(new_BST)
print('=================================================')
print(new_BST.delete_entire_tree(new_BST))
print('=================================================')
new_BST.levelorder_traversal(new_BST)

# operations                       time complexity          space complexity
# creating                              O(1)                    O(1)
# insert                                O(logN)                 O(logN)
# traverse                              O(N)                    O(N)
# search                                O(logN)                 O(logN)
# delete                                O(logN)                 O(logN)
# delete entire tree                    O(1)                    O(1)

