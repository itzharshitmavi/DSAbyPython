# recursion a way of solving a problem by having a function calling itself
# performing the same operations multiple times with different input
# in every step we try smaller inputs to make the problem smaller
# base condition is needed to stop the recursion, otherwise infinite loop will occur
# choose when -> 1. if we can divide the problem into similar (sub)problems then we can use recursion (Sub problem must be similar)
# 2. the prominent usage of recursion in data structure like trees and graphs
# 3. code to list the n...
# 4.implement a method to compute all
# 5. design an algorithm to compute nth...
# 6. It was used in many algorithms (divide and conquer, greedy and dynamic programing)
# 7. interviews
# 8. when we are fine with overhead(both time and space) that comes with it
# 9. when we need a quick working solution instead of efficient one
# 10. when we use memoization in recursion
# when traverse a tree
# space efficient - No
# time efficient - No
# easy to code - Yes
# avoid when -> 1. it can be slow
# 2. when time and space complexity matters for you
# 3. it uses more memory. if we use embedded memory.

# FACTORIAL
def factorial(n):
    assert n >= 0 and int(n) == n, 'the number must be positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(100))

# FIBONACCI NUMBER
def fibonacci(n):
    assert n >=0 and int(n) == n, 'the number cannot be negative or non integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))

# SUM OF GIVEN DIGIT NUMBERS
def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'the number has to ne positive integer only'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n / 10))
print(sum_of_digits(545))

# CALCULATE POWER OF NUMBER
def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'the exponent must be integer only'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp-1)

# GCD (GREATEST COMMON DIVISOR)
def gcd(a,b):
    assert int(a) == a and int(b) == b, 'the numbers must be integer only'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(48,18))

# CONVERT FROM DECIMAL TO BINARY
def decimal_to_binary(n):
    assert int(n) == n, 'the parameter must be an integer only'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n / 2))
print(decimal_to_binary(-13))

# FLATTEN SOLUTION
def flatten(arr):
    result_arr = []
    for custom_item in arr:
        if type(custom_item) is list:
            result_arr.extend(flatten(custom_item))
        else:
            result_arr.append(custom_item)
    return result_arr

print(flatten([1,2,3,[4,5]]))
print(flatten([1, [2, [3, 4], [[5]]]]))
print(flatten([[1], [2], [3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))

# IS PALINDROME SOLUTION
def is_palindrome(str):
    if len(str) == 0:
        return True
    if str[0] != str[len(str) - 1]:
        return False
    return is_palindrome(str[1 :-1])

print(is_palindrome('awesome'))
print(is_palindrome('foobar'))
print(is_palindrome('tacocat'))
print(is_palindrome('amanaplanacanalpanama'))
print(is_palindrome('amanaplanacanalpandemonium'))

# NESTED EVEN SUM
def nested_even_sum(obj, sum = 0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nested_even_sum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]
    return sum

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}
obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}
print(nested_even_sum(obj1))
print(nested_even_sum(obj2))

# PRODUCT OF ARRAY
def product_of_array(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product_of_array(arr[1 :])

print(product_of_array([1,2,3,4,5,6]))
print(product_of_array([45,6,88,9,5]))

# RECURSIVE RANGE
def recursive_range(num):
    if num <= 0:
        return 0
    return num + recursive_range(num - 1)

print(recursive_range(6))

# REVERSE THE STRING
def reverse_string(str):
    if len(str) <= 1:
        return str
    return str[len(str) - 1] + reverse_string(str[0 : len(str) - 1])

print(reverse_string('python'))
print(reverse_string('appmillers'))

# SOME RECURSIVE
def some_recursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return some_recursive(arr[1 :], cb)
    return True
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

print(some_recursive([1,2,3,4,5], is_odd))
print(some_recursive([5,6,7,8,9], is_odd))

# STRINGIFY NUMBER
def stringfyi_number(obj):
    new_obj = obj
    for key in new_obj:
        if type(new_obj[key]) is int:
            new_obj[key] = str(new_obj[key])
        if type(new_obj[key]) is dict:
            new_obj[key] = stringfyi_number(new_obj[key])
    return new_obj

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
print(stringfyi_number(obj))

# FIND THE BIGGEST NUMBER IN ARRAY
def find_the_biggest_number(arr):
    biggest_number = arr[0]
    for index in range(1, len(arr)):
        if arr[index] > biggest_number:
            biggest_number = arr[index]
    print(biggest_number)

print(find_the_biggest_number([2,1,55,14,666,74,89,5569,2222,55,449,656566]))
print(find_the_biggest_number([1,2,3,4,5,6,7,8,9]))
