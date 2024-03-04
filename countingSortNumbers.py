def countingsort(array):
    #finding maximum element of input array
    M = max(array)

    #initiailising count array
    count = [0] * (M + 1)

    #mapping each element of input array as an index of count array
    for num in array:
        count[num] += 1

    #calculating prefix sum at every index of count array
    for i in range(1, M + 1):
        count[i] += count[i - 1]

    #creating output array from count
    output = [0] * len(array)

    for i in range(len(array) - 1, -1, -1):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
    return output

array = [3, 4, 12, 1, 3, 4, 9, 5, 5]
output = countingsort(array)
print('Sorted Array is')
print(output)

#edgecase for already sorted array
#will have to check for sorting one time to see whether the array
#is sorted or not before the algorithm is executed. If it is,
#then exit the loop
