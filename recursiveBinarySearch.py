#recursive binary search
def binarySearch(array, l, r, element):
    #checking base case
    if r >= 1:
        mid = l + (r - 1) // 2

        #checking if element is at the middle element
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            return binarySearch(array, l, mid-1, element)
        else:
            return binarySearch(array, mid+1, r, element)
    else:
        return -1

array = [2, 3, 4, 10, 12]
element = 10

result = binarySearch(array, 0, len(array)-1, element)

if result != -1:
	print("Element is present at index", result)
else:
	print("Element is not present in array")
