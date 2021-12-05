def insertion_sort(arr):

	for i in range(1, len(arr)):

		key = arr[i]
		j   = i - 1

		while j >= 0 and arr[j] > key:

			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = key

	return arr


def test_insertion_sort():

	arr = [3,4,1,2,6,9,7,8]

	for i in range(len(arr)):
		print('Unsorted values in arr are: ', arr[i])

	insertion_sort(arr)
	for j in range(len(arr)):
		print('Sorted values in arr are: ', arr[j])
