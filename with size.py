# creating a stack using python list with limit
class Stack_with_limit:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    # isEmpty
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
    # isFull
    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False
    # push
    def push(self, value):
        if self.is_full():
            return 'the stack is full'
        else:
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

custom_stack1 = Stack_with_limit(4)
print(custom_stack1.is_empty())
print(custom_stack1.is_full())
custom_stack1.push(1)
custom_stack1.push(2)
custom_stack1.push(3)
print(custom_stack1)
# operations                       time complexity          space complexity
# creating stack                        O(1)                    O(1)
# push                                  O(1)/O(n^2)             O(1)
# pop                                   O(n)                    O(1)
# peek                                  O(1)                    O(1)
# isEmpty                               O(n)                    O(1)
# delete entire stack                   O(1)                    O(1)
