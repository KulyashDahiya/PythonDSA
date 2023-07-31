n = 4
for i in range(1, n+1):
    temp = n
    for j in range(1, i):
        print(temp, end='')
        temp = temp - 1
    print()