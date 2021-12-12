import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################


def binary_search(arr, el):

	#######################################
	# The array passed must be sorted ! ! !
	#######################################

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


###############################
# Driver code here !
###############################


arr = [1,3,6,5,7,9,8]
if binary_search(arr, 5):
	print('We found the element ! Hurray !')
else:
	print('We found no element...doh !')