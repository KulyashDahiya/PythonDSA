def zeroesToEnd_N(n: int, arr: list) -> list:
    arr2 = []
    for i in range(n):
        if arr[i] != 0:
            arr2.append(arr[i])

    nz = len(arr2)

    for i in range(nz):
        arr[i] = arr2[i]
    
    for i in range(nz, n):
        arr[i] = 0

    return arr

def zeroesToEnd_TwoPointer(n: int, arr: list[int]) -> list[int]:
    for k in range(n):
        if arr[k] == 0:
            i, j = k, k+1
        
    for t in range(j, n):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    return arr


arr = list(map(int, input().split()))
n = len(arr)

zeroesToEnd_N(n, arr)