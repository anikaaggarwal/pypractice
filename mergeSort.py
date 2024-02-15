def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    arr1 = [0] * (n1)
    arr2 = [0] * (n2)

    for i in range(0, n1):
        arr1[i] = arr1[p + i]

    for j in range(0, n2):
        arr2[j] = arr2[q + 1 + j]

    i = 0
    j = 0
    k = 1

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

        while i < n1:
            arr[k] = arr1[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = arr2[j]
            j += 1
            k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

arr = [4, 7, 22, 54, 56, 88, 99, 345]
n = len(arr)
print('given array')
for i in range(n):
    print(arr)

mergeSort(arr, 0, n-1)
print('Sorted array')
for i in range(n):
    print(arr[i])
