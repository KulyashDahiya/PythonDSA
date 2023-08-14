# A
# BC
# CDE
# DEFG

# rows to be printed = n
# columns to be printed in every row = i
#what to print =

n = int(input())

i = 1
while i<=n:
    j = 1
    start_char = chr(ord('A') + i - 1)
    while j<=i:
        char = chr(ord(start_char) + j - 1)
        print(char, end='')
        j += 1
    print()
    i += 1