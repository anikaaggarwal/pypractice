def countingsort(arr, place):
    n = len(arr)

    output = [0] * (n)

    count = [0] * 10
    #storing count of occurences
    for i in range(0,n):
        index = (arr[i]/place)
        count[int((index)%10)] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    #building the output array
    i = n-1
    while i>=0:
        index = (arr[i]/place)
        output[count[ int((index)%10) ] - 1] = arr[i]
        count[int((index)%10)] -= 1
        i -= 1

    #storing sorted array in original array
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    maximum = max(arr)

    place = 1
    while maximum // place > 0:
        countingsort(arr, place)
        place *= 10


arr = [ 329, 457, 657, 839, 436, 720, 355]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i])

#edge case, for sorted array as input, will have to go through
#the steps to put it into buckets and, not as efficient
