n = int(input())
x = list(map(int, input().split()))
sumX = 0
for i in x:
    sumX += (i - round(sum(x)/n)) ** 2
print(sumX)
