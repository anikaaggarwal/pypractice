def heapify(arr, N, i):
largest = i #initialise largest as root node of the heap
l = 2 * i + 1
r = 2 * i + 2

if l < N and arr[largest] < arr[l]:
    largest = l

if r < N and arr[largest] < arr[r]:
    largest = r
