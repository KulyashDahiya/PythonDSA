## For n = 4
#    1
#   121
#  12321
# 1234321
#  12321
#   121
#    1

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end='')
        j += 1

    j = 1
    while j <= i:
        print(j, end='')
        j += 1

    j = 1
    k = i - 1
    while j < i:
        print(k, end='')
        j += 1
        k -= 1

    print()
    i += 1

i = n
while i >= 1:
    j = 1
    while j <= n - i:
        print(" ", end='')
        j += 1
    j = 1
    while j <= i:
        print(j, end='')
        j += 1

    j = 1
    k = i - 1
    while j < i:
        print(k, end='')
        j += 1
        k -= 1

    print()
    i -= 1