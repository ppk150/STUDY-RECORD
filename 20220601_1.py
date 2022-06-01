
A = input()

A = int(A)

B = []

count = 1

rest = 1

count_rest = 0

B = list(map(int,input().split() ))

if A <= 100:

    for b in range(len(B)):

        y = B[b]

        for i in range(2,y) :

            if y != 1 :
                if y % (i) == 0:
                    count = 0
                    break

        if y != 1 :
            if count != 0:
                count_rest = count_rest +1

        count = 1

print(count_rest)