# rows to be printed = n
# columns to be printed in every row = i
#what to print = stating from (A + n -1 )th char

n = int(input())
k = n
i = 1
while i<=n:
    j = 1
    start_char = chr(ord('A') + k - 1)
    while j<=i:
        char = chr(ord(start_char) + j - 1)
        print(char, end='')
        j += 1
    print()
    k -= 1
    i += 1