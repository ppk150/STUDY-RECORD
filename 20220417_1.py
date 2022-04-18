
k = input()

k = int(k)

Knum = range(k)

NUMlist = []

CAL = []

ave = 0

count = 0

for i in Knum :
    N = input()
    NUM = int(N)
    NUMlist.append(NUM)
    NUMlist.sort()

for h in Knum:

    CAL.append(NUMlist[count]/NUMlist[-1]*100)

    ave = ave + CAL[count]
    count +=1

print(ave/k)