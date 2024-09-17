arr = [8,4,2,90,121,22,345,1]
arr = [-40,1,99,0,99999]
n = len(arr)
arr.sort()
l, sl = arr[n - 1], -1
for i in reversed(arr):
    if i < l:
        sl = i
        break
print(sl)