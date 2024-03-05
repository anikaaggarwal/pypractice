#recursive binary search
def binarySearch(array, l, r, element):
    print('in Binary Search', 'l', l, 'r', r)
    #checking base case
    if r >= 1:
        mid = l + (r - 1) // 2
        print('mid is',mid)
        #checking if element is at the middle element
        if array[mid] == element:
            print('middle element matched')
            return mid
        #if element is smaller, present in left subarray
        elif array[mid] > element:
            print('search on the left')
            return binarySearch(array, l, mid-1, element)
        #if element is greater than mid, present in right subarray
        else:
            print('search on the right')
            return binarySearch(array, mid+1, r, element)
    else:
        print('not found')
        return -1

array = [2, 3, 4, 10, 12, 40]
element = 1

result = binarySearch(array, 0, len(array)-1, element)

if result != -1:
	print("Element is present at index", result)
else:
	print("Element is not present in array")

#not working for odd array size and if the search element is present in the left subarray
