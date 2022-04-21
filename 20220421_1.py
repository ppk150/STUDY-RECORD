
s = input()

sum = len(s)

sum = range(sum)

ALPA= "abcdefghijklnmopqrstuvwxyz"

Arange = len(ALPA)

Arange = range(Arange)

S =[]

for i in ALPA :

    if i in s:
        index = s.find(i)
        S.append(index)
    else :
        S.append(-1)

for i in Arange :
    print(S[i], end = " ")
