# by definition sorting refers to arrange data in a particular format: either ascending or descending
# practical use of sorting-:
# 1. Microsoft Excel: bulit in function to sort data
# 2. online stores: online shopping websites generally have option for sorting by price, review, ratings...
# types of sorting-:
#                           sorting
#                   /                       \
#               space used                  stability
#            /            \                /           \
#      in place        out of place     stable        unstable
# --space used--
# - in place sorting -: sorting algorithms which does not require any extra space for sorting. eg., bubble sort
# - out place sorting -: sorting algorithms which requires an extra space for sorting. eg., merge sort
#--stability--
# - stable sorting -: if a sorting algorithm after sorting the contents does not change the sequence of similar content in which they appear, then this sorting is called stable sorting. eg., insertion sort
# - unstable sorting -: if a sorting algorithm after sorting the content changes the sequences of similar content in which they appear, then it is called unstable sorting. eg., quick sort
#--sorting terminology--
# 1. increasing order -> if successive element is greater than the previous one. eg., 1,3,5,7,9,11
# 2. decreasing order -> if successive element is less than the prevoius one. eg., 11,9,7,5,3,1
# 3. non-increasing order -> if successive element is less than or equal to its previous element in the sequence. eg., 11,9,7,5,5,3,1
# 4. non-decreasing order -> if successive element is greater than or equal to its previous elements. eg.,1,3,5,7,7,9,11

# NAME             TIME COMPLEXITY              SPACE COMPLEXITY            STABLE
# bubble sort           O(n^2)                          O(1)                  yes
# selection sort        O(n^2)                          O(1)                   no
# insertion sort        O(n^2)                          O(1)                   yes
# bucket sort           O(n logn)                       O(n)                   yes
# merge sort            O(n logn)                       O(n)                    yes
# quick sort            O(n logn)                       O(n)                    no
# heap sort             O(n logn)                       O(1)                    no

