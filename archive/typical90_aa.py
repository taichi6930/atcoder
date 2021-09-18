n = int(input())
sList = set()

for i in range(n):
    s = input()
    if s not in sList:
        print(i + 1)
    sList.add(s)
