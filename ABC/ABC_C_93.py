alphaList = sorted(list(map(int, input().split())))
a, b, c = alphaList[0], alphaList[1], alphaList[2]

cnt = int((b-a)/2)
a += cnt * 2

cnt += c - a + int((b - a) % 2)

print(cnt)
