

N = input()

N = int(N)

k = range(N)

gradelist = []

newgradelist = []

count = 0

newcount = 0

ave = 0

PER = []

for i in k :

    Num = list(map(int, input().split()))
    j = range(Num[0])


    for h in j:
        grade = Num[h+1]
        gradelist.append(grade)
        newgradelist.append(gradelist[h])

        ave = ave +gradelist[count]

        count +=1

    for h in j :

        if newgradelist[h] > ave/int(Num[0]):

            newcount += 1

    PER.append(round(newcount/count*100,3))

    count = 0

    newcount = 0

    ave = 0

    gradelist = []

    newgradelist = []

for i in k :
    print(f'{PER[i]:.3f}%')




