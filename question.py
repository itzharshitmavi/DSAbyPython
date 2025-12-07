# write a code to remove duplicates form an unsorted linked list
from Linked_List import linked_list, Node
def remove_duplicate(li):
    if li.head is None:
        return
    else:
        current_node = li.head
        visited = set([current_node.value])
        while current_node.next:
            if current_node.next.value in visited:
                current_node.next = current_node.next.next
            else:
                visited.add(current_node.next.value)
                current_node = current_node.next
        return li

def remove_duplicate_(li):
    if li.head is None:
        return
    current_node = li.head
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
            current_node = current_node.next
        return li.head

custom_ll = linked_list()
custom_ll.generate(10,0,99)
print(custom_ll)
# remove_duplicate(custom_ll)
# print(custom_ll)
remove_duplicate_(custom_ll)
print(custom_ll)

# write a code for return Nth to last
def nth_to_last(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

custom_ll1 = linked_list()
custom_ll1.generate(10,0,99)
print(custom_ll1)
print(nth_to_last(custom_ll1,3))

# write a code to partition a linked list around a value x, such that all nodes less than x come before all nodes greate or equal to x
def partition(ll, x):
    current_node = ll.head
    ll.tail = ll.head
    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < x:
            current_node.next = ll.head
            ll.head = current_node
        else:
            ll.tail.next = current_node
            ll.tail = current_node
        current_node = next_node
    if ll.tail.next is not None:
        ll.tail.next = None

custom_ll2 = linked_list()
custom_ll2.generate(10,0,99)
print(custom_ll2)
partition(custom_ll2,50)
print(custom_ll2)

# you have two numbers represented by a linked list, where each node contains a single digit.
# the digits are stored in reverse order, such that the 1's digit is at the head of the list. write a function that
# adds teh two numbers and returns the sum as a linked list
def sun_list(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = linked_list()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    return ll

llA = linked_list()
llA.add(7)
llA.add(1)
llA.add(6)
llB = linked_list()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sun_list(llA, llB))

# given two (singly) linked lists determine if the two lists intersect. Return the intersecting node. Note that the
# intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact
# same node (by reference) as the jth node if the second linked list, then they are intersecting
def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longer_node = longer.head
    shorter_node = shorter.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
    return longer_node
# helper addition method
def add_same_node(llA, llB, value):
    temp_node = Node(value)
    llA.tail.next = temp_node
    llA.tail = temp_node
    llB.tail.next = temp_node
    llB.tail = temp_node

llA1 = linked_list()
llA1.generate(3,0,10)
llB1 = linked_list()
llB1.generate(4,0,10)
add_same_node(llA1,llB1, 11)
add_same_node(llA1, llB1, 14)
print(llA1)
print(llB1)
print(intersection(llA1, llB1))
