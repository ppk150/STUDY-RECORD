

N = input()

N = int(N)

k = range(N)

gradelist = []

newgradelist = []

count = 0

newcount = 0

ave = 0

for i in k :

    Num = input()
    Num = int(Num)
    j = range(Num)

    for h in j:
        grade = input()
        grade = int(grade)
        gradelist.append(grade)
        newgradelist.append(gradelist[h])

        ave = ave +gradelist[count]

        count +=1

    for h in j :

        if newgradelist[h] > ave/int(Num):

            newcount += 1
    print(round(newcount/count*100,3))

    count = 0

    newcount = 0

    ave = 0

    gradelist = []

    newgradelist = []

