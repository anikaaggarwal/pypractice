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

    #building the output arrya
    i = n-1
    while i>=0:
        index = (arr[i]/place)
        output[count[ int((index)%10) ] - 1] = arr[i]
        count[int((index)%10)] -= 1
        i -= 1

    #storing sorted array in original arrya
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
