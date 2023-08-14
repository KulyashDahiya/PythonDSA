#Write Your Code Here
N = input()
l = len(N) - 1

rev = ""

while l != -1:
    if N[l] == 0:
        continue
    else:
        rev = rev + N[l]

    l -= 1

print(int(rev))