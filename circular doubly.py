# time and space complexity of doubly linked list :-
# operations                       time complexity          space complexity
# creation                              O(1)                    O(1)
# insertion                             O(n)                    O(1)
# traversing(forward, backward)         O(n)                    O(1)
# searching                             O(n)                    O(1)
# deletion of node                      O(n)                    O(1)
# deletion of linked list               O(n)                    O(1)
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
class circular_doubly_ld:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
# creation of circular doubly linked list
    def create_CDLL(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        return 'the CDLL is created successfully'
# insertion method in list
    def insert_CDLL(self, value, location):
        if self.head is None:
            return 'the CDLL does not exists'
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
        return 'the node ha been successfully created'
# traverse a list
    def traverse_CDLL(self):
        if self.head is None:
            print('there is not any node in list')
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next
# reverse traverse a list
    def reverse_traverse_CDLL(self):
        if self.head is None:
            print('there is not any node for traversal')
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev
# search in list
    def search_CDLL(self, node_value):
        if self.head is None:
            print('there is not any element in CDLL')
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                if temp_node == self.tail:
                    return 'the value does not exist in CDLL'
                temp_node = temp_node.next
# delete a node in list
    def delete_CSLL(self, location):
        if self.head is None:
            print('there is not any element in CDLL')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head =  None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            print('the node is successfully deleted')
# delete entire list
    def delete_entire_CDLL(self):
        if self.head is None:
            print('there is not any element to delete')
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print('the CDLL is successfully deleted')

circular_doubly_linked_list = circular_doubly_ld()
circular_doubly_linked_list.create_CDLL(5)
print([node.value for node in circular_doubly_linked_list])
circular_doubly_linked_list.insert_CDLL(0,0)
circular_doubly_linked_list.insert_CDLL(1,1)
circular_doubly_linked_list.insert_CDLL(2,2)
print([node.value for node in circular_doubly_linked_list])
circular_doubly_linked_list.traverse_CDLL()
circular_doubly_linked_list.reverse_traverse_CDLL()
print(circular_doubly_linked_list.search_CDLL(2))
circular_doubly_linked_list.delete_CSLL(0)
print([node.value for node in circular_doubly_linked_list])
circular_doubly_linked_list.delete_CSLL(-2)
print([node.value for node in circular_doubly_linked_list])
circular_doubly_linked_list.delete_entire_CDLL()
print([node.value for node in circular_doubly_linked_list])
