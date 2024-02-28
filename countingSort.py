def countingsort(A):
    #output char array to store sorted output
    output = [0 for i in range(256)]
    #count array to store count of individual characters
    count = [0 for i in range(256)]

    ans = ["" for _ in A]

    for i in A:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(A)):
        output[count[ord(A[i])] - 1] = A[i]
        count[ord(A[i])] -= 1

    for i in range(len(A)):
        ans[i] = output[i]
    return ans

A = "introductiontoalgos"
ans = countingsort(A)
print('Sorted Array is')
print("".join(ans))
