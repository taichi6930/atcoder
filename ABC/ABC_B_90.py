a, b = map(int, input().split())
num = 0
for i in range(a, b + 1):
    if str(i) == str(i)[::-1]:
        num += 1

print(num)
