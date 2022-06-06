
B = list(map(int, input().split()))

ERA = [True] * (int(B[1])+1)
ERA[0] = False
ERA[1] = False

for i in range(2, (B[1]+1)):
    if ERA[i] == True :
        j = 2

        while (i*j) <= B[1] :
            ERA[i*j] = False
            j +=1

for i in range(B[0], len(ERA)):
    if ERA[i] ==True:

        print(i)

