import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################


def binary_search(el, arr:list=None) -> bool:

	'''
	Binary search algo searches an element into an array by splitting this array in two parts and 
	checking if the element is lower or bigger/equal than the element in the middle.
	If the element is lower/bigger than the element in the middle, the algo keeps on splitting the
	lowest/biggest part of the array until the value in the middle of the splitted array is EQUAL 
	to the element we are searching out.
	Given the nature of the algo, the array must be sorted first.

	param el: element to be searched into the array passed as argument
	param arr: list of element 
	'''

	l = 0
	r = len(arr) - 1

	arr = quick_sort(arr)

	while l <= r:

		mid = round((r + l) / 2)
		if arr[mid] == el:
			return True
		elif el < arr[mid]:
			r = mid - 1
		else:
			l = mid + 1

	return False