# Check Prime

n = int(input())

for i in range(2, (n//2 + 2)):
    if n % i == 0:
        print("Non Prime")
        break
else:
    print("Prime")
