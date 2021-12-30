def selection_sort(arr):

	n     = len(arr)

	for i in range(n):
		start = i
		for j in range(i + 1, n):
			if arr[j] < arr[start]:
				start = j

		arr[i], arr[start] = arr[start], arr[i]

	return arr


arr = [-19,14,7,6,4,8,7,11,1,12]
print(selection_sort(arr))