import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################


def jump_search(el, arr:list=None) -> bool:

	'''
	Jump search algo is searching an element "block by block": if the element is bigger than the last value 
	at array block N, it keeps on searching the next block until the element searched is lower.
	Once the block is found, within the block it applies linear search to find it the element is actually there.
	The Big O for this algo is linear therefore O(n).

	param arr: list of element 
	param el: element to be searched into the array passed as argument
	'''

	if arr == None:
		print('Array passed is None, please pass an array and retry.')
		return

	arr     = quick_sort(arr)
	n       = len(arr)
	block   = int( n ** 0.5 )
	counter = block

	# Let's check block by block if the element is present or not !
	for i in range(block, n, block):

		if el == arr[i]:
			return True
		elif el < arr[i]:
			
			for j in range(counter - block, counter, 1):
				if el == arr[j]:
					return True
			return False
		counter += block

	# At a certain moment, we have index of looping (counter) that gets bigger than array length.
	# ... as long as we found no element before !
	if counter >= n:
		for j in range(n - block, n, 1):
			if el == arr[j]:
				return True
		return False


arr = [1,2,3,4,5,6,7,8,9,10,12,15,16,17,11]
print(jump_search(13, arr))



