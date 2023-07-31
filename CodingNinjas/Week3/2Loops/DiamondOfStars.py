n = int(input())

n1 = n//2 + 1
n2 = n//2

for i in range(1, n1 + 1):
    for j in range(n1-i):
        print(" ", end='')
    for j in range(1, 2*i):
        print("*", end='')
    print()
for i in range(n2, 0, -1):
    for j in range(n2 -i + 1):
        print(" ", end='')
    for j in range(1, 2*i):
        print("*", end='')
    print()
