def partition(arr, low, high):

    i     = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):

    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def test_quick_sort():

    arr = [2,1,5,4,3,9,8,6,7]
    n   = len(arr)

    for i in range(n):
        print('Unsorted array is ', arr[i])


    quick_sort(arr, 0, n - 1)
    for j in range(n):
        print('Sorted array is ', arr[j])