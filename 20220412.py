
x = input()

y = input()

x = int(x)

y = int(y)


if x > 0 and y > 0 :
    print("1사분면")
elif x < 0 and y > 0 :
    print("2사분면")
elif x < 0 and y < 0 :
    print("3사분면")
elif x > 0 and y < 0 :
    print("4사분면")
    
