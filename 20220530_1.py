
A = input()

A = int(A)

B = []

count = 0

rest = 1

count_rest = 0

for i in range(A) :


    k = input()

    k = int(k)

    B.append(k)

for b in range(len(B)):
    if B[b]!= 1 :
        Y = round((B[b]**(1/2)))

        for y in range(Y) :

            rest = rest +1

            if B[y] % rest != 0 :

                count_rest = 1

            elif B[y] % Y == 0 :

                count_rest = 0

        if count_rest > 0 :
            count = count +1

    rest = 0

print(count)