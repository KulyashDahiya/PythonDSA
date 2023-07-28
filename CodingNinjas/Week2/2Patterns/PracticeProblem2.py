# 4555
# 3455
# 2345
# 1234

# rows to be printed = n
# columns to be printed in every row = n
#what to print = starting in every row k = n-i+1 , increment if k<=n

n = int(input())

i = 1
while i <= n :
    j = 1
    k = n - i + 1
    while j <= n:
        print(k, end='')
        j += 1
        if k <= n:
            k += 1

    print()
    i += 1