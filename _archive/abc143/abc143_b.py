n = int(input())
d = list(map(int, input().split()))

dSum = sum(d) ** 2

for i in d:
    dSum -= i ** 2

print(dSum // 2)
