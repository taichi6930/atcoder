N = list(input())
leftHands = set(list('12345'))
rightHands = set(list('67890'))

ans = 500
nowFigure = N[0]

for i in range(1, len(N)):
    nextFigure = N[i]

    # 同じ指なら301msかかる
    if nowFigure == nextFigure:
        ans += 301
        continue

    nowHand = 'l' if nowFigure in leftHands else 'r'
    nextHand = 'l' if nextFigure in leftHands else 'r'

    # 同じ手なら210msかかる
    ans += 210 if nowHand == nextHand else 100
    nowFigure = nextFigure

print(ans)
