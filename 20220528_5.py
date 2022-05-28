

N = int(input())

k = 0

end = 1

count = 0

while end :

    if N % 5 == 0 :
        k = count + N /5
        print(int(k))

        end = 0

    N -=3

    count = count + 1


    if N == 0:
        print(count)
        end = 0

    if N < 0 :

        print(-1)
        end = 0


