def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [31, 41, 59, 26, 41, 58]
insertionSort(arr)
print(arr)

#if the input array is already sorted
#the inner loop never executes

#if the input array is sorted in reverse order, then the inner
#loop executes the maximum possible times, so the running time
#is as bad as possible O(n^2)
