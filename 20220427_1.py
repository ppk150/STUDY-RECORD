
S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

STR = input()

count = 0

for i in STR :
    if i in S[0:3]:
        count +=3
    elif i in S[3:6]:
        count +=4
    elif i in S[6:9]:
        count +=5
    elif i in S[9:12]:
        count +=6
    elif i in S[12:15]:
        count +=7
    elif i in S[15:18]:
        count +=8
    elif i in S[18:21]:
        count +=9
    elif i in S[21:25]:
        count +=10
    else:
        print ("알파벳 대분자로 입력좀...")

print(count)