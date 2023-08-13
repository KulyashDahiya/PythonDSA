n = input()
l = len(n)

sum = 0
for i in n:
    sum = sum + pow(int(i), l)

if int(n) == sum:
    print("true")
else:
    print("false")