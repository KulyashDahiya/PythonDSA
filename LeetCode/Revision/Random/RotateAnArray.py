# Rotate an Array

def rotateArray(arr: list, n: int, k: int) -> list[int]:
    temp = arr[0:n-k]
    arr =  arr[n-k:] + temp
    return arr
    


arr = list(map(int, input().split()))
k = int(input())
n = len(arr)


rotateArray(arr, n, k)