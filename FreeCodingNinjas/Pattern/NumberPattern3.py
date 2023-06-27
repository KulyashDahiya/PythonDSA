#L8 YT

def printPatt(n):
    for i in range(n):
        s = i + 1
        for j in range(i + 1):
            print(s + j, end="")
        print()

def printPatt1(n):
    res = []
    for i in range(n):
        s = ""
        a = i + 1
        for j in range(i+1):
            s = s + str(a)
            a += 1
        res.append(s)
    return res

n = 4
print(printPatt1(n))