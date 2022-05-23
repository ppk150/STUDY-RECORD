
T = input()

Tnum = int(T)

k = range(Tnum)



FLOOR = 0

ROOM = 0

#몫 = 층  , 나머지 =  방 호수

for i in k :

    H = input()

    Hnum = int(H)

    W = input()

    Wnum = int(W)

    N = input()

    Nnum = int(N)

    FLOOR = Nnum % Hnum

    ROOM =  Nnum // Hnum +1


    print (100*FLOOR+ ROOM)




