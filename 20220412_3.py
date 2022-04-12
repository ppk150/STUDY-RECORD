
D1 = input("첫 번째 주사위: ")

D2 = input("두 번째 주사위: ")

D3 = input("세 번째 주사위: ")

D1 = int(D1)

D2 = int(D2)

D3 = int(D3)

if D1 > 6 or D2 >6 or D3 > 6:
    print("1~6까지의 숫자를 입력하세요.")
    
    D1 = input("첫 번째 주사위: ")

    D2 = input("두 번째 주사위: ")

    D3 = input("세 번째 주사위: ")
    
    D1 = int(D1)

    D2 = int(D2)

    D3 = int(D3)


ALL = []

ALL = [D1 ,D2, D3]

ALL.sort()

if D1 == D2 == D3 :
    prize = 10000 + 1000* D1

if D1 == D2 and D1 != D3 :
    prize = 1000 + 100 * D1
elif D1 != D2 and D2 == D3:
    prize = 1000 + 100 * D2
elif D1 == D3 and D2 != D3:
    prize = 1000 + 100 * D3

if D1 != D2 and D1 != D3 and D2 != D3:
    prize = ALL[2] * 100

print("수령 상금 : ", prize)
    
