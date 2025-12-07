# creating stack using linked list
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next
class Linked_list:
    def __init__(self):
        self.head = None
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
class Stack_with_linked_list:
    def __init__(self):
        self.Linked_list = Linked_list()
    def __str__(self):
        values = [str(x.value) for x in self.Linked_list]
        return '\n'.join(values)
        # isEmpty
    def is_empty(self):
        if self.Linked_list.head == None:
            return True
        else:
            return False
    # push
    def push(self, value):
        node = Node(value)
        node.next = self.Linked_list.head
        self.Linked_list.head = node
    # pop
    def pop(self):
        if self.is_empty():
            return 'there is not any element in the stack'
        else:
            node_value = self.Linked_list.head.value
            self.Linked_list.head = self.Linked_list.head.next
            return node_value
    # peek
    def peek(self):
        if self.is_empty():
            return 'there is not any element in the stack'
        else:
            node_value = self.Linked_list.head.value
            return node_value
    # delete
    def delete(self):
        self.Linked_list.head = None

custom_stack2 = Stack_with_linked_list()
print(custom_stack2.is_empty())
custom_stack2.push(1)
custom_stack2.push(2)
custom_stack2.push(3)
print(custom_stack2)
custom_stack2.pop()
print(custom_stack2)
print(custom_stack2.peek)
custom_stack2.delete()
# operations                       time complexity          space complexity
# creating stack                        O(1)                    O(1)
# push                                  O(1)                    O(1)
# pop                                   O(1)                    O(1)
# peek                                  O(1)                    O(1)
# isEmpty                               O(1)                    O(1)
# delete entire stack                   O(1)                    O(1)
