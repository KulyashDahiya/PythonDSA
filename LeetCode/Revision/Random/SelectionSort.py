# SELECTION SORT

def selectionSort(arr, n):
    for i in range(n):
        min_j = i
        for j in range(i+1, n):
            if arr[j] < arr[min_j]:
                min_j = j
        arr[i], arr[min_j] = arr[min_j], arr[i]

    print(arr)


n = int(input())
arr = list(map(int, input().split()))
# n = 5
# arr = [5, 2, 3, 1, 4]
selectionSort(arr, n)