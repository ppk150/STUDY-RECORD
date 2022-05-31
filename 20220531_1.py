
A = input()

A = int(A)

B = []

count = 0

rest = 1

count_rest = 0


B = list(map(int,input().split() ))


for b in range(len(B)):
    if B[b]!= 1 :
        Y = round((B[b]**(1/2)))

        for y in range(Y) :

            rest = rest + 1

            if B[b] % rest != 0 :

                count_rest = count_rest + 1

            elif B[b] % Y == 0 :

                count_rest = 0
                break


        if count_rest > 0:
            count = count +1

    rest = 0

print(count)