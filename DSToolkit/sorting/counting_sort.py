def counting_sort(arr):

    # 1. Get the length of the array and create zero element array (no numpy.zeros here !)
    n      = len(arr)
    count  = [0] * max(arr)

    # 2. Count element repetition of the passed array
    for i in range(n):
        count[ arr[i] - 1] += 1

    # 3. Get the cumulative counting array created at step 3
    for i in range(1, len(count)):
        count[i] = count[i] + count[i - 1]

    # 4. Given cumulated array, get its index passing array element ant put it into returned array
    output = [0] * n
    for i in range(n):
        j = count[ arr[i] - 1 ]
        output[j - 1] = arr[i]
        count[ arr[i] - 1 ] -= 1

    return output


arr = [1,3,4,9,2,5,1,1,6,2,9,2,11,11,16,16]
print( counting_sort(arr) )