n = int(input())
check = [input()]
flg = True
for i in range(n-1):
    w = input()
    if check[-1][-1] != w[0] or w in check:
        flg = False
        break
    check.append(w)

print("DRAW" if flg else "WIN" if i % 2 == 0 else"LOSE")
