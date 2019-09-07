n = int(input())
maxCityName = ""
maxCityNum = 0
sumCityNum = 0
for i in range(n):
    s, p = map(str, input().split())
    p = int(p)
    sumCityNum += p
    if maxCityNum < p:
        maxCityName = s
        maxCityNum = p

print(maxCityName if maxCityNum * 2 > sumCityNum else "atcoder")
