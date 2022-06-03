B = list(map(int,input().split() ))


if B[1] >= B[2] :
    print("-1")

else:
    C = B[0]/(B[2]-B[1])
    print(int(C)+1)