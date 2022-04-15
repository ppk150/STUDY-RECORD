
N =input()

Num = int(N)

k = range(Num)

y = []

for i in k:
    H = input()
    Hnum = int(H)
    y.append(Hnum)
    y.sort()

print(y[0],y[Num-1])

