def linearSearch(array, length, element):

    for i in range(0, length):
        if (array[i] == element):
            return i
    return -1

array = [21, 32, 14, 110, 35]
element = 1110
length = len(array)

result = linearSearch(array, length, element)
if (result == -1):
    print('Element not found in the array')
else:
    print('Element is found at index', result)
