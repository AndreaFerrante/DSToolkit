def partition(arr, low, high):

    i     = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def sort(arr, low, high):

    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition(arr, low, high)
        sort(arr, low, pi - 1)
        sort(arr, pi + 1, high)


def quick_sort(arr):

    n   = len(arr)
    sort(arr, 0, n - 1)

    return arr