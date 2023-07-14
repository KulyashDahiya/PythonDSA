import numpy as np
n = int(input())
#arr = list[int(item) for item in input().split()]
lst = [int(item) for item in input().strip().split()]
k = int(input())

lst = lst[k:]+lst[:k]
arr = np.array(lst)

print(arr)