a = int(input())
b = int(input())

for i in range(a, 10 ** 18 + 1):
    if not str(a) in str(i):
        continue
    if not str(b) in str(2 * i):
        continue
    print(i)
    break
