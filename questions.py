# what is the runtime of the code below
# def foo(arr):
#     sum = 0----------->O(1)
#     product = 0------->O(1)
#     for i in arr:------>O(n)
#         sum += i-------->O(1)
#     for i in arr:--------->O(n)
#         product *= i------>O(1)
#     print("sum = " + str(sum) + " product = " + str(product))---->O(1)
# time complexity = O(N)

# def print_pair(arr):
#     for i in arr:---------->O(n^2)
#         for j in arr:------------>O(n)
#             print(str(i) + ", " + str(j))----->O(1)
# time complexity = O(n^2)

# def print_unordered_pair(arr):
#     for i in range(0, len(arr)):
#         for j in range(i + 1, len(arr)):
#             print(arr[i] + " ," + arr[j])
# 1. counting the iteration          2. average work
# 1st ----> n - 1                    outer loop ---> N times
# 2nd -----> n - 2                    inner loop?
#       |                               1st --> 10 }
# (n - 1)+(n - 2)+(n - 3)+--+2+1         2nd --> 9 } = 5 ---> 10/2
#  n(n - 1)/2                                |     } n ----> n/2
# n^2/2 + n                                   1    }
# n^2                                      n*n/2 = n^2/2 ---> O(N^2)
# time complexity = O(N^2)

# def print_unordered_pair(arrA, arrB):
#     for i in range(len(arrA)):
#         for j in range(len(arrB)):
#             if arrA[i] < arrB[j]: ---------------------------> O(1)
#                 print(str(arrA[i] + ", " + str(arrB[j])))---->O(1)
# b = len(arrA) , a = len(arrB)
# time complexity = O(ab) multiply runtime

# def print_unordered_pairs(arrA, arrB):
#     for i in range(len(arrA)):------------\
#                                            |---->O(ab)
#         for j in range(len(arrB)):--------/
#             for K in range(0, 100000):------------->O(1)
#                 print(str(arrA[i]) + ", " + str(arrB[j]))--->O(1)
# 1000000 will still constant, a = len(arrA), b = len(arrB)
# time complexity = O(ab)

# def reverse(arr):
#     for i in range(0, int(len(arr)/2)):-------->O(N/2) -->O(N)
#         other = len(arr) - i - 1--------------->O(1)
#         temp = arr[i]------------------------->O(1)
#         arr[i] = arr[other]----------------------->O(1)
#         arr[other] = temp---------------------->O(1)
#     print(arr)---------------------------------O(1)
# time complexity = O(N)

# def factorial(n):------------------->M(n)
#   if n < 0:         }
#       return -1     }___________> O(1)
#   elif n == 0:      }
#       return 1      }
#   else:
#       return n * factorial(n - 1) ------------>M(n - 1)
# M(n) = O(1) + M(n - 1)
# M(O) = O(1)
# M(n - 1) = O(1) + M((n - 1) - 1)
# M(n - 2) = O(1) + M((n - 2) - 1)
# M(n) = 16 M(n -1)
# 1 + (1+ M((n - 1) - 1)
# 2 + M(n - 2)
# 2 + M((n - 2) - 1)
# 3 + M(n - 3)
# a + M(n - a)
# n + M(n - n)
# n + 1
# n
# so time complexity = O(N)

# def all_fib(n):
#     for i in range(n):
#         print(str(i) + ":, " + str(fib(i)))
#
# def fib(n):
#     if n <= 0:
#         return 0 ----------->time complexity of this function(branches^depth)= O(2^N)
#     elif n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# so time complexity = O(2^N)

# def power_of_2(n):
#     if n < 1:
#         return 0
#     elif n == 1:  -------> total area = O(1)
#         print(1)
#         return 1
#     else:
#         prev = power_of_2(int(n / 2))
#         curr = prev * 2  }
#         print(curr)      }------->O(1)
#         return curr      }
# time complexity = O(log N)

# which of the following are equivalent to O(N) why?
# 1. O(N + P), where P < N/ 2 -------->O(N)  ✔ (remove P)
# 2. O(2N) -------------------> O(N) ✔ (remove 2)
# 3. O(N + log N) --------------> O(N) ✔ (remove log N)
# 4. O(N + N log N) -------------->O(N log N) ❌ (remove N)
# 5. O(N + M) ----->❌ (both are variables and there is no function like M in the graph)
