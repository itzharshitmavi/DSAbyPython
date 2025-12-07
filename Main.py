# Big O is the language and metric we use to describe the efficiency of algorithm
# Time complexity -> it is a way of showing how the runtime of function increases as the size of input increases
# types -> O(N), O(N²), O(2^N)
# physical is constant but electronic increases linearly (with the size of file)
# best case -> O(N)
# worst case -> O(N²)
# average case -> O(N log N)
# type of Big O -:
# 1. Big O -> it is a complexity that is going to be less ot equal to the worse case (Big O - O(N))
# 2. Big Ω (Omega) -> it is a complexity that is going to be at least more than the best case (Big Ω - Ω(1))
# 3. Big θ (theta) -> it is a complexity that is within bounds og the worst and the best cases (Big θ - θ(n/2))
# algorithm rum time complexities -:
# complexity                name                    sample
# O(1)                     constant              accessing a specific element in array
# O(N)                     linear                loop through element array
# O(log N)                 logarithmic           find an element in sorted array
# O(N²)                    quadratic             looking at an every index in the array twice
# O(2^N)                   exponential           double recursion in fibonacci
# drop constant and non dominant terms. ex-:
# drop constant -> O(2N) ----> O(N)
# drop non dominant terms -> 1. O(N^2 + N) -----> O(N^2), 2. O(N + log N) ----> O(N), 3. O(2*2^N + 1000N^100) -----> O(2^N)
# why use drop constant and non dominant?
# 1. it is very possible that O(N) code is faster than O(1) code for specific inputs
# 2. different computers with different architecture have different constant factors -------> 1. fast computer, fast memory access, lower constant, 2. slow computers, slow memory access, higher constant
# 3. different algorithms with the same basic idea and computational complexity might have slightly different constants. ex -> 1. a*(b-c) vs a*b - a*c
# as n ----> ♾️, constant factors are not really a big deal
# when do we multiply the tun times and when do we add them?
# example explanation -> 1. for a in arrA:           2. for a in arrA
#                               print(a)                    for b in arrB
#                           for b in arrB                       print(a,b)
#                               print(b)
#                    add the runtime: O(A + B)            multiply the runtime: O(A*B)
# if your algorithm is in the form "do this, then when you are done, do that" then you add the runtimes
# if your algorithm is in the form "do this for each time you do that" then you multiply the runtimes
# how to measure the codes using Big O?
# rules -:
# 1. any assignment statement and if statement that are executed once regardless of the size of the problem (complexity -> O(1))
# 2. a simple "for" loop from 0 to n (with no internal loops) (complexity - O(n))
# 3. a nested loop of the same type takes quadratic time complexity (complexity - O(n^2))
# 4. a loop, in which the controlling parameter is divided by two at each step (complexity - O(log n))
# 5. when dealing with multiple statements, just add them up
# ex-> def find_the_biggest_number(arr):
#     biggest_number = arr[0] -------------------------------------> O(1)
#     for index in range(1, len(arr)): ----------------->O(n)\
#         if arr[index] > biggest_number: ----->O(1)\          |---->O(n)
#                                                     |->O(1)/
#             biggest_number = arr[index] ----->O(1)/
#     print(biggest_number) ---------------------------------------->O(1)
# time complexity : O(1) + O(n) + O(1) = O(n)
# how to measure recursive algorithm?
# def findMaxNumRec(sampleArray, n): --------------------------------------------------> M(n)
#    if n == 1: ---------------------------------------------------------------------->O(1)
#       return sampleArray[0] -------------------------------------------------------->O(1)
#    return max(sampleArray[n - 1], findMaxNumRec(sampleArray, n - 1)) --------------->M(n - 1)
# explanation: M(n) = O(1) + M(n - 1)    }                M(n) = 1 + M(n - 1)
#  M(1) = O(1)                           }                 = 1 + (1 + M(n - 1) - 1))
# M(n -1) = O(1) + M((n -1) - 1)         }                 = 2 + M(n + 2)
# M(n - 1) = O(1) + M((n -1) -1)         }                 = 2 + 1 M((n - 2) - 1)
# M(n -2) = O(1) + M((n - 2) - 1)        }                 = 3 + M(n - 3)
#                                       we can write it as:  = a + M(n - a)
#                                       put (a = n - 1): = n - 1 + M(n - (n - 1))
#                                                          = n - 1 + 1
#                                                          = n
# how to measure recursive algorithm that make multiple calls?
# def f(n):
#     if n <= 1:
#         return 1
#     return f(n - 1) + f(n - 1)
# let say for 4                         f(4) ----------------> 0
#                                     /      \
#                                   /          \
#                                 f(3)           f(3) --------> 1
#                               /   \               / \
#                            /        \           /     \
#                          f(2)        f(2)    f(2)      f(2) --> 2
#                         /  \         /  \       / \       / \
#                       /      \      /    \     /   \     /    \
#                      f(1)    f(1)   f(1) f(1)  f(1) f(1) f(1)  f(1) -> 3
# so, O(branches^depths) so in given examples O(2^4)

array = [1, 2, 3, 4, 5]

######  Constant time complexity  #######
print('######  Constant time complexity  #######')
print(array[0])

######  Linear time complexity  #######
print('######  Linear time complexity  #######')
for element in array:
    print(element)

######  Logarithmic time complexity  #######
print('######  Logarithmic time complexity  #######')
for index in range(0, len(array), 3):
    print(array[index])

######  Quadratic time complexity  #######
print('######  Quadratic time complexity  #######')
for x in array:
    for y in array:
        print(x, y)

######  Exponential time complexity  #######
print('######  Exponential time complexity  #######')


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


######  Add vs Multiply #######
arrayA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arrayB = [11, 12, 13, 14, 15, 16, 17, 18, 19]

for a in arrayA:
    print(a)

for b in arrayB:
    print(b)

for a in arrayA:
    for b in arrayB:
        print(a, b)

######  Iterative algorithm - finding the biggest number in the array #######

sample1Array = [1, 10, 45, 33, 23, 45, 67, 2, 3, 33, 55, 11, 65, 76, 34, 35, 27, 99]


def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1, len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    print(biggestNumber)


findBiggestNumber(sample1Array)


######  Recursive algorithm - finding the biggest number in the array #######

def findMaxNumRec(sampleArray, n):
    if n == 1:
        return sampleArray[0]
    return max(sampleArray[n - 1], findMaxNumRec(sampleArray, n - 1))


print(findMaxNumRec(sample1Array, len(sample1Array)))


######  Recursive algorithm multiple calls #######

def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 1)


print(f(3))


######  Quiz Questions #######


def f1(n):
    if n <= 0:
        return 1
    else:
        return 1 + f1(n - 1)


def f2(n):
    if n <= 0:
        return 1
    else:
        return 1 + f2(n - 5)


def f3(n):
    if n <= 0:
        return 1
    else:
        return 1 + f3(n / 5)


def f4(n, m, o):
    if n <= 0:
        print(n, m, o)
    else:
        f4(n - 1, m + 1, o)
        f4(n - 1, m, o + 1)


def f5(n):
    for i in range(0, n, 2):
        print(i)
    if n <= 0:
        return 1
    else:
        return 1 + f5(n - 5)

