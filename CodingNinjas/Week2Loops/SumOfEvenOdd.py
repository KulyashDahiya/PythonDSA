## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)

n = input()

Esum, Osum = 0, 0

for i in n:
    if int(i) % 2 == 0:
        Esum = Esum + int(i)
    else:
        Osum = Osum + int(i)

print(Esum," ",Osum)
