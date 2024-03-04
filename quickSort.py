def partition(array, low, high):
    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i+1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

input = [1, 7, 4, 3, 20, 27, -5]
print("Unsorted Array is")
print(input)

n = len(input)
quickSort(input, 0, n-1)
print("Sorted Array after quicksort is")
print(input)

#edge case where the array is already sorted, the pivot will be
#the smallest or largest element in the array
#which means worst case scenario, so it would not improve
#the efficiency of the process if you use quick sort on an already
#sorted array
