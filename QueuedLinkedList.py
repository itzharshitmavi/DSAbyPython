# creating queue by using linked list
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
class queue_by_linked_list:
    def __init__(self):
        self.linked_list = linked_list()
    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)
    # enqueue
    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node
    # isEmpty
    def is_empty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False
    # dequeue
    def dequeue(self):
        if self.is_empty():
            return 'there is not any node in the queue'
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            return temp_node
    # peek
    def peek(self):
        if self.is_empty():
            return 'their is no element in this queue'
        else:
            return self.linked_list.head
    # delete
    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None

custom_queue2 = queue_by_linked_list()
custom_queue2.enqueue(1)
custom_queue2.enqueue(2)
custom_queue2.enqueue(3)
custom_queue2.enqueue(4)
print(custom_queue2)
print(custom_queue2.dequeue())
print(custom_queue2)
print(custom_queue2.peek())
custom_queue2.delete()
# operations                       time complexity          space complexity
# creating                              O(1)                    O(1)
# enqueue                               O(1)                    O(1)
# dequeue                               O(1)                    O(1)
# peek                                  O(1)                    O(1)
# isEmpty                               O(1)                    O(1)
# delete entire queue                   O(1)                    O(1)
