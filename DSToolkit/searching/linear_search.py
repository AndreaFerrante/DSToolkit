def linear_search(el, arr:list=None) -> bool:

	'''
	Linear search algo is searching literally an element inside and array.
	The Big O for this algo is linear therefore O(n).

	param arr: list of element 
	param el: element to be searched into the array passed as argument
	'''

	if arr is None:
		print('Please, pass an array first.')
		return

	n   = len(arr)

	for i in range(n):
		if el == arr[i]:
			return True

	return False