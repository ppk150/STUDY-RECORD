T = input()

Tnum = int(T)

k = range(Tnum)

S= []


FLOOR = 0

ROOM = 0

#몫 = 층  , 나머지 =  방 호수
# B[0] = H ,B[1] = W, B[2] = N

for i in k :
    B = list(map(int, input().split()))

    FLOOR = B[2] % B[0]

    ROOM = B[2] // B[0] + 1

    if FLOOR ==0 :
        FLOOR = B[0]
        ROOM= B[2] // B[0]


    S.append(100*FLOOR+ ROOM)

for i in k :
    print (S[i])

