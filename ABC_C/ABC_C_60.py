n, t = map(int, input().split())
tList = list(map(int, input().split()))
tSum = t

for i in range(n-1):
    tElapse = tList[i+1] - tList[i]
    tSum += (t if tElapse > t else tElapse)

print(tSum)
