
M = input()

M = int(M)


N = input()

N = int(N)

B = []

count = 1

K = N - M

count_rest = 0

SUM = 0 # 찾아낸 소수의 합을 담는 변수
SUMARRY = [] # 찾아낸 소수를 담는 배열

for b in range(M , N+1):
    B.append(b)  # N~M 배열 생성

if M == N :                 # M=N 일때 예외 처리 하는 코드
    for i in range(2,M) :

        if M != 1 :
            if M % (i) == 0:
                count = 0
                break

    if M != 1 :
        if count != 0:
            count_rest = count_rest +1
            SUMARRY.append(M)
            SUM = SUM + M
else:

    for k in range(K+1) :  # N, M의 차 만큼 동작하게 하는 함수

        y = B[k]

        if y != 1 :
            count = 0

            if y == 2 or y == 3 or y == 5 or y == 7 :
                SUMARRY.append(y)

            if y % 2 == 0 or y % 3 == 0 or y % 5 == 0 or y % 7 == 0:
                count = 0

            else :
                SUMARRY.append(y)
                count = 1


for  i in range(len(SUMARRY)):
    print(SUMARRY[i])
