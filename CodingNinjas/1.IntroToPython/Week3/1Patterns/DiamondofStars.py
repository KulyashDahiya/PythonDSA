##       N should always be odd

n = int(input())
if n%2 == 0:
    print("Invalid : You entered an even number.")
    exit()

n1 = n//2 + 1
n2 = n//2

i = 1
while i <= n1:
    j = 1
    while j <= n1 - i:
        print(" ", end='')
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end='')
        j += 1
    print()
    i += 1
i = n2
while i >= 1:
    j = 1
    while j <= n2 - i + 1:
        print(" ", end='')
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end='')
        j += 1
    print()
    i -= 1
