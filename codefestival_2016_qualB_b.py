n, a, b = map(int, input().split())
S = list(input())

cntIn = 0
cntOut = 0

for s in S:
    if s == "c":
        print("No")
        continue
    if cntIn + cntOut >= a + b:
        print("No")
        continue
    if s == "a":
        cntIn += 1
    if s == "b":
        if cntOut >= b:
            print("No")
            continue
        cntOut += 1
    print("Yes")
    continue
