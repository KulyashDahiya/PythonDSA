
n = int(input())

for i in range(1, n+1):
    k = i
    for j in range(1, n+1):
        if j < i:
            print(" ", end='')
        else:
            print(k, end='')
            k += 1
    print()

for i in range(1, n):
    for j in range(1, n+1):
        if j < n - i:
            print(" ", end='')
        else:
            print(j, end='')
    print()