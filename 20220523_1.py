
T = input()

end = 1

count = 0

Tnum = int(T)

a = range(1,15)
aa = range(2,15)

p= [[0 for _ in range(15)] for _ in range(15)]

count = 0

for i in a :
    p[0][i] = i
    p[i][1] = 1


for i in a  :
    for j in aa:
        p[i][j] = p[i][j-1]+p[i-1][j]


while(end):
    A = input()
    A = int(A)
    B = input()
    B = int(B)

    print(p[A][B])
    count = count + 1

    if Tnum == count :
        end = 0

