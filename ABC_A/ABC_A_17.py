sum = 0
for i in range(3):
    s, e = map(int, input().split())
    sum += s//10 * e
print(sum)
