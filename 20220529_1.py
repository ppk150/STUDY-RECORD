
A = int(input())

B = []

count = 0

count_rest = 0

flag = 0

for i in range(A) :


    k = int(input())

    B.append(k)

    for b in range(len(B)):

        Y = int(B[i]**(1/2))

        for y in range(Y) :



            if B[i] % Y != 0 :

                count_rest = count_rest +1

            if B[i] % Y == 0 :
                break

            if Y == 0:
                break

            Y = Y - 1

        if count_rest == Y :
            flag = 1
        else :
            flag = 0

    if flag == 1 :
        count += 1

print(count)











