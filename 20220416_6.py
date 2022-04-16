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

    for h in k :
        if Nrest[h] == Nrest[k]:
            del Nrest[h]

f = len(Nrest)

print(f)
