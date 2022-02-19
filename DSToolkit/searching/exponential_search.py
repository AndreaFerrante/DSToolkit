import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################


import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################


# Python program to find an element x in a sorted array using Exponential Search
# A recursive binary search function returns location  of x in given array arr[l..r] is present, otherwise -1

def binarySearch( arr, l, r, x):

    if r >= l:

        mid = ( r + l ) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        return binarySearch(arr, mid + 1, r, x)

    return -1
 
# Returns the position of first occurrence of x in array
def exponentialSearch(arr, n, x):

    # IF x is present at first location itself
    if arr[0] == x:
        return 0
         
    # Find range for binary search j by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
     
    # Call binary search for the found range
    return binarySearch( arr, i // 2, min(i, n - 1), x)