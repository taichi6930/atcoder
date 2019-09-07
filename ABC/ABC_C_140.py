a = int(input())
b = list(map(int, input().split()))
aSum = b[-1] + b[0]
for i in range(a-2):
    aSum += min(b[i], b[i+1])
print(aSum)
