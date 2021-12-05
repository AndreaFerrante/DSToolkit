def bubble_sort(arr):

	n = len(arr)
	for i in range(n - 1):
		for j in range(n - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

	return arr


def test_bubble_sort():

	arr = [3,4,1,2,6,9,7,8]

	for i in range(len(arr)):
		print('Unsorted values in arr are: ', arr[i])

	bubble_sort(arr)
	for j in range(len(arr)):
		print('Sorted values in arr are: ', arr[j])