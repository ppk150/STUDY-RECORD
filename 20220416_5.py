k = range(10)

Nlist = []

Nrest = []

count = 0

j = len(Nrest)

CL = range(j)

for i in k:
    N = input()
    Num = int(N)
    Nlist.append(Num%42)
    Nrest.append(Nlist[i])

F = set(Nrest)
FF = len(F)
print(FF)
