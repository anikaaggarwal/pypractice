def bucketSort(array):
    bucket = []

    #create empty buckets
    for i in range(len(array)):
        bucket.append([])

    #insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    #sort the elements of each bucket
    for i in range(len(array)):
           bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

array = [.42, .32, .33, .52, .37, .48, .51]
secondArray = [24, 87, 1, 44, 23, 311, 67, 99, 134]
print('Sorted Array is')
print(bucketSort(array))
