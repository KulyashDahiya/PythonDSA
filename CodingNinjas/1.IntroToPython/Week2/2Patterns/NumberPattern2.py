# 1
# 11
# 202
# 3003

n = int(input())

i = 1
while i <= n :
    j = 1
    while j <= i:
        if i == 1:
            print("1",end='')
            break
        elif (j == 1) or (j == i):
            print(i-1, end='')
        else:
            print("0", end='')
        j += 1

    print()
    i += 1

