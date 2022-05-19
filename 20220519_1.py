
A = input()
Anum = int(A)

B = input()
Bnum = int(B)

C = input()
Cnum = int(C)

count = 0

end = 1

while end  :
    count = count + 1

    if  Bnum  > Cnum  :
        print('-1')
        end = 0

    if Anum + Bnum * count < Cnum * count :

        print(count)

        end = 0



