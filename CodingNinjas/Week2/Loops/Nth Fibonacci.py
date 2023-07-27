
n = int(input())
f, b = 1, 1

for i in range(n - 2):
    if n == 1 or n == 2:
        break
    a = f
    f = f + b
    b = a

print(f)