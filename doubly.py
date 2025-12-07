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
class doubly_ld:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
# creation of doubly linked list
    def create_DLL(self, node_value):
        node = Node(node_value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'the DLL is created'
# insertion method in doubly
    def inset_node(self, node_value, location):
        if self.head is None:
            print('the node cannot be inserted')
        else:
            new_node = Node(node_value)
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == 1:
                new_node.next = None
                new_node.prev = self.tail
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
# traversal through list
    def traverse_DLL(self):
        if self.head is None:
            print('there is not any element to traverse')
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
# reverse traverse
    def reverse_traverse_DLL(self):
        if self.head is None:
            print('there is not any element to traverse')
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev
# search in doubly list
    def search_DLL(self, node_value):
        if self.head is None:
            return 'there is not any element in list'
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                temp_node = temp_node.next
            return 'the node does not exits in the list'
# deleting node in list
    def delete_node(self, location):
        if self.head is None:
            print('there is not any element in DLL')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            print('the node has been successfully deleted')
# delete entire list
    def delete_entire_DLL(self):
        if self.head is None:
            print('there is not any node in DLL')
        else:
            temp_node = self.tail
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print('the DLL is successfully deleted')
doubly_linked_list = doubly_ld()
doubly_linked_list.create_DLL(5)
print([node.value for node in doubly_linked_list])
doubly_linked_list.inset_node(0,0)
doubly_linked_list.inset_node(2,1)
doubly_linked_list.inset_node(6,2)
print([node.value for node in doubly_linked_list])
doubly_linked_list.traverse_DLL()
doubly_linked_list.reverse_traverse_DLL()
print(doubly_linked_list.search_DLL(5))
doubly_linked_list.delete_node(0)
print([node.value for node in doubly_linked_list])
doubly_linked_list.delete_node(-1)
print([node.value for node in doubly_linked_list])
doubly_linked_list.delete_entire_DLL()
print([node.value for node in doubly_linked_list])
