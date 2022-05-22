
A = input()

Anum = int(A)

B = input()

Bnum = int(B)

V =input()

Vnum = int(V)

climb = 0

count = 0

end = 1

while end :

    climb = climb + Anum
    count = count + 1

    if Vnum < climb :
        print(count)

        end = 0

    climb = climb - Bnum







