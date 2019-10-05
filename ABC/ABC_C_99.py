n = int(input())
six = [6, 42, 258, 1554, 9330, 55986]
nine = [9, 90, 819, 7380, 66429]
nMin = 100000
for i in range(6):
    for j in range(5):
        ans = six[i] + nine[j]
        ansCnt = i + j + 2 + (n-ans)
        if nMin > ansCnt and ans <= n:
            nMin = ansCnt
print(nMin)
