n = int(input())

i, k = 1, n
while i <= n:
    j = 1
    while j <= n - i + 1:
        print(k, end='')
        j += 1

    print()
    k -= 1
    i += 1
