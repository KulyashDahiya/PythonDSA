#  1     1
#   2   2
#    3 3
#     4
#    3 3
#   2   2
#  1     1

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= 2 * n - i:
        if (j == i) or (j == (2 * n) - i):
            print(i, end='')
        else:
            print(" ", end='')
        j += 1
    print()
    i += 1

i = 1
k = n - 1
while i <= n - 1:
    j = 1
    while j <= n+i:
        if (j == k) or (j == k + 2*i):
            print(k, end='')
        else:
            print(" ", end='')
        j += 1
    print()
    k -= 1
    i += 1