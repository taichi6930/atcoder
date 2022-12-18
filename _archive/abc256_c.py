h1, h2, h3, w1, w2, w3 = map(int, input().split())
ans = 0

for a1 in range(1, 31):
    for a2 in range(1, 31):
        a3 = h1 - a1 - a2
        if a3 <= 0:
            break
        for a4 in range(1, 31):
            a7 = w1 - a1 - a4
            if a7 <= 0:
                break
            for a5 in range(1, 31):
                a6 = h2 - a4 - a5
                a8 = w2 - a2 - a5
                a9 = h3 - a7 - a8
                if a9 != w3 - a3 - a6:
                    break
                if min(a1, a2, a3, a4, a5, a6, a7, a8, a9) > 0:
                    ans += 1

print(ans)
