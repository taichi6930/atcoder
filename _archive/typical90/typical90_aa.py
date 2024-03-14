n = int(input())
se = set()
for i in range(n):
    s = input()
    if not s in se:
        print(i + 1)
        se.add(s)
