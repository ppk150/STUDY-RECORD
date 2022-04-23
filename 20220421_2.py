
N = input()

Num = int(N)

S = input()

Snum = len(S)

Srange = range(Snum)

Sint = int(Snum)

SS = []

count =0

alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"

for k in S:
    count = 0
    for i in alphanumeric :
        if i == S[count]:
            SS.append(k)
            count += 1
            
for k in Srange :

    print(SS[k]*Num,end ="" )