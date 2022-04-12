
H = input("시간 (hour) 입력")

M = input("분 (minute) 입력")

H = int(H)

M = int(M)

Total = H*60+M

Totalmodify = Total-45

TH = Totalmodify//60

if TH < 0 :
    TH = 23

TM = Totalmodify % 60   

print(TH ,':', TM)
