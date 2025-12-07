# time and space complexity of circular singly linked list :-
# operations                       time complexity          space complexity
# creation                              O(1)                    O(1)
# insertion                             O(n)                    O(1)
# traversing                            O(n)                    O(1)
# searching                             O(n)                    O(1)
# deletion of node                      O(n)                    O(1)
# deletion of linked list               O(1)                    O(1)
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
class circular_singly_ld:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
# creation of Circular SLL
    def create_CSSL(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return 'the CSLL has been created'
# insertion in linked list
    def insert_CSLL(self, value, location):
        if self.head is None:
            return 'the head reference is null'
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.tail.next
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
            return 'the node has been successfully inserted'
# traversal of a linked list
    def traversal_CSLL(self):
        if self.head is None:
            print('there is not any element for traversal')
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break
# searching in linked list
    def search_CSLL(self, node_value):
        if self.head is None:
            return 'there is not any node in CSLL'
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return 'the node does not exists in this CSLL'
# deletion of linked list
    def delete_CSLL_node(self, location):
        if self.head is None:
            print('there is not any node in CSLL')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
# delete entire list
    def delete_entire_CSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None

circular_singly_linked_list = circular_singly_ld()
circular_singly_linked_list.create_CSSL(0)
circular_singly_linked_list.insert_CSLL(0,0)
circular_singly_linked_list.insert_CSLL(2,1)
circular_singly_linked_list.insert_CSLL(3,1)
circular_singly_linked_list.insert_CSLL(4,2)
print([node.value for node in circular_singly_linked_list])
circular_singly_linked_list.traversal_CSLL()
print(circular_singly_linked_list.search_CSLL(2))
print(circular_singly_linked_list.search_CSLL(6))
circular_singly_linked_list.delete_CSLL_node(0)
print([node.value for node in circular_singly_linked_list])
circular_singly_linked_list.delete_CSLL_node(2)
print([node.value for node in circular_singly_linked_list])
circular_singly_linked_list.delete_entire_CSLL()
print([node.value for node in circular_singly_linked_list])
