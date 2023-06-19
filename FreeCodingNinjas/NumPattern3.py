def numPatt3(n):
    res = []
    for i in range(n):
        s = ""
        for j in range(i+1):
            if j==0 or j==i:
                s += "1"
            else:
                s += "2"
        res.append(s)
    return res


n = 4
print(numPatt3(n))