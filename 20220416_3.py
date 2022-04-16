
k =range(3)

Nlist = []

for i in k :
    N = input()
    Num = int(N)
    Nlist.append(Num)

CAL = Nlist[0]*Nlist[1]*Nlist[2]

CALINDEX = CAL

CALLIST= str(CALINDEX)

L = len(CALLIST)

a = range(10)

CL = range(L)

countlist = []

count = 0

for j in a:

    for h in CL:

        if int(CALLIST[h]) == j:
            count +=1

    print(count)
    count = 0