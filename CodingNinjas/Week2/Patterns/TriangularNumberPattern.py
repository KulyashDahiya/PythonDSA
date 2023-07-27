# 1
# 22
# 333
# 4444

n = int(input())

#No. of rows = n
#No. of columns = i
#What to print = i

i = 1
while i<=n:
    j = 1
    while j<=i:
        print(i, end='')
        j += 1
    print()
    i += 1