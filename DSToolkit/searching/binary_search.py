def bubble_sort(arr):

	n = len(arr)
	for i in range(n - 1):
		for j in range(n - i- 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	return arr



def binary_search(arr, el):

	#######################################
	# The array passed must be sorted ! ! !
	#######################################

	l = 0
	r = len(arr) - 1

	arr = bubble_sort(arr)

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
if binary_search(arr, 4):
	print('We found the element ! Hurray !')
else:
	print('We found no element...doh !')