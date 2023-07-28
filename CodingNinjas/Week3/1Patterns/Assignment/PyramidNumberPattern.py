#    1
#   212
#  32123
# 4321234

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n-i:
        print(" ", end='')
        j += 1

    j = 1
    k = i
    while j <= i:
        print(k, end='')
        k -= 1
        j += 1

    j = 1
    k = 2
    while j <= i-1:
        print(k, end='')
        k += 1
        j += 1

    print()
    i += 1