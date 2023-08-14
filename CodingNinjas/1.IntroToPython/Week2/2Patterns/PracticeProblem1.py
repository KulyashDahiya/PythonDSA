# 12344321
# 123**321
# 12****21
# 1******1

# rows to be printed = n
# columns to be printed in every row = 2n
#what to print = * when

n = int(input())

i = 1
while i <= n :
    j = 1
    while j<= n - i + 1:
        print(j, end='')
        j += 1

    j = 1
    while j <= i-1:
        print("*", end='*')
        j += 1

    j = n - i + 1
    while j >= 1:
        print(j, end='')
        j -= 1

    print()
    i += 1