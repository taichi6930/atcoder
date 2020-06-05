import math as m

x = int(input()) - 1
flg = 1
while flg == 1:
    flg = 0
    x += 1
    a = int(m.sqrt(x)//1 + 1)
    for i in range(2, a):
        if x % i == 0:
            flg = 1
            break

print(x)
