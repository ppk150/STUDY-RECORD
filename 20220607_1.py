
B = int(input())

NewB = B

ERA = [True] * (B+1)
ERA[0] = False
ERA[1] = False

S = []

AS = []

ASK = 1
ASNUM =0
end = 1

k = 0

for i in range(2, (B+1)):
    if ERA[i] == True :
        j = 2

        while (i*j) <= B :
            ERA[i*j] = False
            j +=1

for i in range(len(ERA)):
    if ERA[i] ==True:
        S.append(i)


while end :


    if NewB % S[k] == 0 :
        AS.append(S[k])
        ASK = ASK*AS[ASNUM]
        ASNUM = ASNUM +1
        NewB = NewB / S[k]

    elif NewB % S[k] != 0 :
        k +=1

    if B == ASK :
        break

for i in range(len(AS)) :
    print(AS[i])







