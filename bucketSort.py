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
