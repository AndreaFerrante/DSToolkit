import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################


def interpolationSearch(arr, lo, hi, x):

	'''
	Interpolation search is an algorithm for searching for a key in an array 
	that has been ordered by numerical values assigned to the keys (key values).
	'''

	# Since array is sorted, an element present in array must be in range defined by corner
	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

		# Probing the position with keeping
		# uniform distribution in mind.
		pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))

		# Condition of target found
		if arr[pos] == x:
			return pos

		# If x is larger, x is in right subarray
		if arr[pos] < x:
			return interpolationSearch(arr, pos + 1, hi, x)

		# If x is smaller, x is in left subarray
		if arr[pos] > x:
			return interpolationSearch(arr, lo, pos - 1, x)

	return -1