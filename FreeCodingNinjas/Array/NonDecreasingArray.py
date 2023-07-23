import numpy as np

def nonDec(arr, n):
    index = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            if (index != -1):
                return False
            index = i

    if (index == -1 or index == 0 or index == n-2):
        return True
    if (arr[index-1]<=arr[index+1]):
        return True
    if (arr[index]<=arr[index+2]):
        return True

    return False


lst = [int(item) for item in input().strip().split()]
arr = np.array(lst)
if nonDec(arr, len(arr)):
    print("True")
else:
    print("False")

# -90 -70 -61 -57 -246 -28 1 14 35 63
#
# -78 -68 -51 -20 187 -182 42 64 66 93