import math as m

a, b = map(int, input().split())
cost = -1
flg = 0

while flg == 0 and cost < 10 ** 6 / 1.5:
    cost += 1
    aAns = m.floor(cost * 0.08)
    bAns = m.floor(cost * 0.1)
    if aAns == a and bAns == b:
        flg = 1
    if a - aAns < 0 or b - bAns < 0:
        break

print(cost if flg == 1 else -1)
