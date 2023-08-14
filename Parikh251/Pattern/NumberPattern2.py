#L8 on YT

def patt(n):
    res =[]
    for i in range(n):
        s = ""
        for j in range(n-i):
            s = s + str(j+1)
        res.append(s)
    return res

n = 4
print(patt(n))