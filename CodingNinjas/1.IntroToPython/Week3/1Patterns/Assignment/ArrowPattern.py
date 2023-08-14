##   N is always odd  ## Space after every *
# *
#  * *
#   * * *
#    * * * *
#   * * *
#  * *
# *

n = int(input())
n1 = n // 2 + 1
n2 = n // 2

i = 1
while i <= n1:
    j = 1
    while j <= (2 * i) - 1:
        if (j <= i - 1):
            print(" ", end='')
        else:
            print("*", end=' ')
        j += 1
    print()
    i += 1

i = n2
while i >= 1:
    j = 1
    while j <= (2 * i) - 1:
        if (j <= i - 1):
            print(" ", end='')
        else:
            print("*", end=' ')
        j += 1

    print()
    i -= 1
