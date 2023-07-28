n = int(input())
i = 1
k = (2*n) + 1
while i <= n:
    j = 1
    while j <= (2*n) + 1:
        if (j == n+1) or (j == i) or (j==k):
            print("*", end='')
        else:
            print("0", end='')
        j += 1

    print()
    k -= 1
    i += 1