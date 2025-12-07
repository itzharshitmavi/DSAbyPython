# linked list is a form of a sequential collections and it does not have to be in order. A linked list is made up if independent nodes that may contain any type of data and each node had a reference to the next node in the link
# nodes of linked list is not continuous
# elements of linked list are independent objects
# the size of linked list is not predefined
# insertion and removals in linked list are very efficient
# types:-
# 1. singly linked list = each node in a list stores the value/data and the references to the next node in the linked list
# 2. circular singly linked list = same as singly linked list but the one difference is the last node of this list stores a reference to the first node,
# in case of singly linked list the last node reference is always null (after reaching to the last node of linked list we have option to go back to the first node) ex. game chances
# 3. doubly linked list = this type of linked list also resembles a single linked list but the difference here is we have two references from each node:-
# a. reference to previous node, b. reference to the next node,
# here we have a option of traverse back as we have a reference to the previous node. Due to the fact that we know the physical location of both previous and next node,
# thus it provides us a flexibility of reversing in both direction ex. song player
# 4. circular doubly linked list = both doubly and circular doubly linked list is similar but the only difference between these two is first and last node,
# it has access to the first node i.e., after reaching to the last node of linked list we have option to go back to the first node,
# this give flexibility of traversing from the first node to the last node and form the last node to the first node ex. using in computers like macs
# location in memory -> even if we know the location of the first node, we cannot find the location of other node by adding value ot current location of the node. because the other node can be anywhere in the memory
# algorithm of creating linked list
#  node value______> - create node_______>  head = none?--------no---------
#   location         - assign value              |                        |
#                                                |yes                     |
#         - head = node <________________________|                        |
#         - tale = node                                                   |
#         |          _____________ - node.next = head <--------yes----location = first
#         |          |             - head = node                          | no
#         |          |                                                    |
#         |___> terminate <---------- - node.next = null<----yes---location = last
#                   ^                 - last.next = node                   |
#                   |                 - tail = node                        | no
#                   |                                                      |
#                   |___________  - find location(loop)  <_________________|
#                                 - current.next = node
#                                 - node.next = nextNode
# time and space complexity of singly linked list :-
# operations                       time complexity          space complexity
# creation                              O(n)                    O(n)
# insertion                             O(n)                    O(1)
# traversing                            O(n)                    O(1)
# searching                             O(n)                    O(1)
# deletion of node                      O(n)                    O(1)
# deletion of linked list               O(1)                    O(1)
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
class Singly_ld:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in linked list
    def insert_sll(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                    next_node = temp_node.next
                    temp_node.next = new_node
                    new_node.next = next_node
                    if temp_node == self.tail:
                        self.tail = new_node
# traverse in singly linked list
    def traverse_sll(self):
        if self.head is None:
            print('the singly linked list does not exists')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
# search in singly linked list
    def search_sll(self, node_value):
        if self.head is None:
            return 'the list does not exists'
        else:
            node = self.head
            while node is not None:
                if node.value == node_value:
                    return node.value
                node = node.next
            return 'the value does not exists in this list'
# delete a node form linked list
    def delete_node(self, location):
        if self.head is None:
            print('the SLL does not exists')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                        self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                    next_node = temp_node.next
                    temp_node = next_node.next

singly_linked_list = Singly_ld()
singly_linked_list.insert_sll(1,1)
singly_linked_list.insert_sll(2,1)
singly_linked_list.insert_sll(3,1)
singly_linked_list.insert_sll(4,1)
singly_linked_list.insert_sll(0,0)
singly_linked_list.insert_sll(5,3)
print([node.value for node in singly_linked_list])
singly_linked_list.traverse_sll()
print(singly_linked_list.search_sll(3))
singly_linked_list.delete_node(0)
# node1 = Node(1)
# node2 = Node(2)
#
# singly_linked_list.head = node1
# singly_linked_list.head.next = node2
# singly_linked_list.tail = node2
