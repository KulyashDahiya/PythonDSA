# *
# **
# ***
# ****

n = int(input())

#No. of rows = n
#No. of columns = i
#What to print = *

i = 1
while i<=n:
    j = 1
    while j<=i:
        print("*", end='')
        j += 1
    print()
    i += 1