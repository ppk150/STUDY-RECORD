


N = input()
N = int(N)
a = []



Num = range(N)

for i in Num:
    aN = input()
    aN = int(aN)
    a.append(aN)

def slolve ( a: list):
    count = 0
    inta = 0
    k = len(a)
    k = range(k)
    for h in k :
        inta +=a[count]
        count +=1

    print(inta)

slolve(a)


