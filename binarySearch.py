#iterative binary search
def binarySearch(array, l, r, element):
    while l <= r:

        mid = l + (r - 1) // 2

        #checking if element is at the middle element
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            l = mid + 1
        else:
            r = mid -1

    return -1

array = [1, 3, 4, 10, 40]
element = 10

result = binarySearch(array, 0, len(array)-1, element)
if result != -1:
    print('Element found at index', result)
else:
    print('Element not in input array')
