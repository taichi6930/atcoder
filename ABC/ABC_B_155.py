n = int(input())
aList = list(map(int, input().split()))
ans = True
for i in aList:
    if i % 2 == 0:
        if not(i % 3 == 0 or i % 5 == 0):
            ans = False
            break

print("APPROVED" if ans else "DENIED")
