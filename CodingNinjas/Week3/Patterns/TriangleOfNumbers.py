n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end='')
        j += 1

    j = 1
    k = i
    while j <= i:
        print(k, end='')
        j += 1
        k += 1

    k = k - 2
    while k >= i:
        print(k, end='')
        k -= 1

    print()
    i += 1