# stack is a data structure that stores item in a Last-in/First-out manner
# we need stack data structure whenever we need the functionality in our application that utilizes the last coming data first
# ex: back button in browser
# stack operations: create stack, push, pop, peek, isEmpty, isFull, deleteStack
# three ways of creating stack -> using list without size limit, using list with size limit and using linked list
# 1. stack using list -> a. easy to implement, b. speed problem when it grows
# 2. stack using linked list -> a. fast performance, b.implementation is not easy

# stack using python list without size
class Stack_without_limits:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    # isEmpty
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
    # push
    def push(self, value):
        self.list.append(value)
        return 'the element has been successfully inserted'
    # pop
    def pop(self):
        if self.is_empty():
            return 'there is not any element in the stack'
        else:
            return self.list.pop()
    # peek
    def peek(self):
        if self.is_empty():
            return 'there is not any element in the stack'
        else:
            return self.list[len(self.list) - 1]
    # delete
    def delete(self):
        self.list = None

custom_stack = Stack_without_limits()
print(custom_stack.is_empty())
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
print(custom_stack)
print(custom_stack.pop())
print(custom_stack)
print(custom_stack.peek())
custom_stack.delete()
# when to use stack?
# 1. LIFO(last in first out) functionality
# 2. the chance of data corruption is minimum
# when to avoid stack?
# 1. random access is not possible
