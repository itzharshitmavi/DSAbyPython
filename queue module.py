# in python, we can create a queue using three different module, which are -:
# 1. collections module, 2. queue module, 3. multiprocessing module
# by collection module
# how to use collections.deque as a FIFO queue?
from collections import deque
custom_queue = deque(maxlen= 3)
print(custom_queue)
custom_queue.append(1)
custom_queue.append(2)
custom_queue.append(3)
print(custom_queue)
custom_queue.append(4)
print(custom_queue)
print(custom_queue.popleft())
print(custom_queue)
custom_queue.clear()
print(custom_queue)

# by queue module
# how to use queue module as FIFO queue?
import queue as q
custom_queue1 = q.Queue(maxsize = 3)
print(custom_queue1.empty())
print(custom_queue1.qsize())
custom_queue1.put(1)
custom_queue1.put(2)
custom_queue1.put(3)
print(custom_queue1.qsize())
print(custom_queue1.full())
print(custom_queue1.get())
print(custom_queue1.qsize())

# by multiprocessing module
# how to use multiprocessing queue as a FIFO queue?
from multiprocessing import Queue
custom_queue2 = Queue(maxsize = 3)
custom_queue2.put(1)
print(custom_queue2.get())
