# describe how you could use a single python list to implement three stacks?
#           _______________|______________|_______________
#           |____|____|____|____|____|____|____|____|____|
#              0    1    2 |  3    4    5 |  6    7    8
# for stack 1 - [0],[1],[2] -----> [0, n/3)
# for stack 2 - [3],[4],[5] -----> [n/3, 2n/3)
# for stack 3 - [6],[7],[8] -----> [2n/3, n)
class multi_stack:
    def __init__(self, stack_size):
        self.number_stack = 3
        self.custom_list = [0] * (stack_size * self.number_stack)
        self.sizes = [0] * self.number_stack
        self.stack_size = stack_size
    def is_full(self, stack_number):
        if self.sizes[stack_number] == self.stack_size:
            return True
        else:
            return False
    def is_empty(self, stack_number):
        if self.sizes[stack_number] == 0:
            return True
        else:
            return False
    def index_of_top(self, stack_number):
        off_set = stack_number * self.stack_size
        return off_set + self.sizes[stack_number] - 1
    def push(self, item, stack_number):
        if self.is_full(stack_number):
            return 'the stack is full'
        else:
            self.sizes[stack_number] += 1
            self.custom_list[self.index_of_top(stack_number)] = item
    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return 'the stack is empty'
        else:
            value = self.custom_list[self.index_of_top(stack_number)]
            self.custom_list[self.index_of_top(stack_number)] = 0
            self.sizes[stack_number] -= 1
            return value
    def peek(self, stack_number):
        if self.is_empty(stack_number):
            return 'the stack is empty'
        else:
            value = self.custom_list[self.index_of_top(stack_number)]
            return value

custom_stack = multi_stack(6)
print(custom_stack.is_full(0))
print(custom_stack.is_empty(1))
custom_stack.push(1,0)
custom_stack.push(2,0)
custom_stack.push(3,2)
print(custom_stack.peek(1))
print(custom_stack.peek(0))

# how would you design a stack which, in addition to push ans pop has a function min which returns the minimum element? push, pop, and min should all operate in O(1)?
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ', ' + str(self.next)
        return string
class stack:
    def __init__(self):
        self.top = None
        self.min_node = None
    def min(self):
        if not self.min_node:
            return None
        return self.min_node.value
    def push(self, item):
        if self.min_node and (self.min_node.value < item):
            self.min_node = Node(value = self.min_node.value, next = self.min_node)
        else:
            self.min_node = Node(value = item, next = self.min_node)
        self.top = Node(value = item, next = self.top)
    def pop(self):
        if not self.top:
            return  None
        self.min_node = self.min_node.next
        item = self.top.value
        self.top = self.top.next
        return item

custom_stack1 = stack()
custom_stack1.push(5)
print(custom_stack1.min())
custom_stack1.push(6)
print(custom_stack1.min())
custom_stack1.push(3)
print(custom_stack1.min())
custom_stack1.pop()
print(custom_stack1.min())

# imagine a (literal) stack of plates. if the stack gts too high, it might topple. therefore, in real life, we would
# likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that
# mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one
# exceeds capacity, SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop()
# should return the same value as it would if there were just a single stack).
# follow up: implement a function popAt(int index) which performs a pop operation on a specific sub - stack.
class plate_stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    def __str__(self):
        return self.stacks
    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    def pop(self):
        while(len(self.stacks) and len(self.stacks[-1])) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
    def pop_at(self, stack_number):
        if len(self.stacks[stack_number]) > 0:
            return self.stacks[stack_number].pop()
        else:
            return None

custom_stack2 = plate_stack(2)
custom_stack2.push(1)
custom_stack2.push(2)
custom_stack2.push(3)
custom_stack2.push(4)
# print('\n',custom_stack2.pop())
print(custom_stack2.pop_at(1))

# implement queue class which implements a queue using two stacks
class stack_queue:
    def __init__(self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def push(self, item):
        self.list.append(item)
    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
class queue_via_stack:
    def __init__(self):
        self.in_stack = stack_queue()
        self.out_stack = stack_queue()
    def enqueue(self, item):
        self.in_stack.push(item)
    def dequeue(self):
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        result = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return result

custom_stack3 = queue_via_stack()
custom_stack3.enqueue(1)
custom_stack3.enqueue(2)
custom_stack3.enqueue(3)
print(custom_stack3.dequeue())
custom_stack3.enqueue(4)
print(custom_stack3.dequeue())

# an animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must
# adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select weather they would
# prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they
# would like. create the data structure to maintain this system and implement operations such as enqueue, dequeue,
# dequeueAny dequeueDog, and dequeueCat
class animal_shelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    def dequeue_cat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat
    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog
    def dequeue_any(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result

custom_queue = animal_shelter()
custom_queue.enqueue('cat1', 'Cat')
custom_queue.enqueue('cat2', 'Cat')
custom_queue.enqueue('dog1', 'Dog')
custom_queue.enqueue('cat3', 'Cat')
custom_queue.enqueue('dog2', 'Dog')
# print(custom_queue.dequeue_cat())
# print(custom_queue.dequeue_dog())
# print(custom_queue.dequeue_dog())
print(custom_queue.dequeue_any())
