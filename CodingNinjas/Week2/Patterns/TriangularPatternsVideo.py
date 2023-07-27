1
23
345
4567

# rows to be printed = n
# columns to be printed in every row = i
#what to print =  (k = i) and k +=1       OR    i + j -1

n = int(input())

i = 1
while i<=n:
    j = 1
    p = i
    while j<=i:
        print(p, end='')
        j += 1
        p += 1
    print()
    i += 1

# OR

# i = 1
# while i<=n:
#     j = 1
#     while j<=i:
#         print(i+j-1, end='')
#         j +=1
#     print()
#     i += 1
