n = 3
arr = [8,4,2]
count = 0
for i in range(n - 1):
    if arr[i] <= arr[i + 1]:
        continue
    else:
        count = count + 1

if count <= 1:
    print("true")
else:
    print("false")


-90 -70 -61 -57 -246 -28 1 14 35 63

-78 -68 -51 -20 187 -182 42 64 66 93