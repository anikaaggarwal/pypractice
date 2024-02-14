def selectionSort(arr, size):

    for i in range(size):
        key = i
        for j in range(i + 1, size):
            if arr[j] < arr[key]:
                key = j

        (arr[i], arr[key]) = (arr[key], arr[i])

arr = [5, 75, 4, -145, -10, 22, -202]
size = len(arr)
selectionSort(arr,size)
print('The sorted array is:')
print(arr)
