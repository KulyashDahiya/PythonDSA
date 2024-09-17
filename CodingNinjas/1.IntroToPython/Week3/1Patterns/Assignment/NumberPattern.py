# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n:
        if j <= i:
            print(j, end='')
        else:
            print(" ", end='')
        j += 1

    j = 1
    k = i
    while j <= n:
        if j > n - i:
            print(k, end='')
        else:
            print(" ",end='')
        k = n - j
        j += 1



    print()
    i += 1