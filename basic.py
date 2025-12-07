# A tree is a nonlinear data structure with hierarchical relationship between its elements without having any cycle, it is basically reversed form of a real life tree
# ex:                                    ----------- Drinks---------
#                             /                                            \
#                       hot                                                  cold
#                    /      \                                              /       \
#               tea          coffee                                 non-alcoholic    alcoholic
#              /   |            /   |   \                           /     |     \      /      \
#           green  black  americano latte cappuccino            cola    fanta   soda wine     beer
# properties of tree:-
# - represent hierarchical data
# - each node has two components: data and a link to its sub category
# - base category sand sub categories under it
# common tree look like this:   n1  --------> root
#           depth 1          /      \ -------> edge
# ancestor of n4 and n7 <- n2--------n3-----> siblings  height of n3 = 1
#           depth 2      /    \         \ -----> edge
#        siblings <-----n4-----n5        n6 ---> leaf
#                     /   \         so total depth for n4 = 2
#                    n7    n8 ----> leaf
# why a tree?
# - quicker and easier access to the data
# - store hierarchical data, like folder structure, organisation structure, XML/HTML data.
# - there are many different type of data structure which performs better in various situations:
# - binary search tree, AVL, red black tree, trie
# tree terminology-:
# Root: top node without parent
# Edge: a link between parent and child
# Leaf: a node which does not have children
# Siblings: children of same parent
# Ancestor: parent, grandparent, great grandparent of a node
# Depth of node: a length of the path from root to node
# Height of node: a length of the path from the node to the deepest node
# Depth of tree: depth of root node (depth of n1 = 0) (basically the depth of tree is always zero)
# Height of tree: height of root node to deepest node
# contrasting difference between depth and height of node: the depth is measured form the root, but the height is
# measured from the node until the deepest node

# GENERAL TREE IN PYTHON
class tree_node:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    def add_child(self, tree_node):
        self.children.append(tree_node)

tree = tree_node('Drinks', [])
cold = tree_node('Cold', [])
hot = tree_node('Hot', [])
tree.add_child(cold)
tree.add_child(hot)
tea = tree_node('Tea', [])
coffee = tree_node('coffee', [])
cola = tree_node('Cola', [])
fanta = tree_node('Fanta', [])
hot.add_child(tea)
hot.add_child(coffee)
cold.add_child(cola)
cold.add_child(fanta)
print(tree)

