m = int(input())
D = list(map(int, input().split()))
mid = (sum(D) + 1) // 2

for i, d in enumerate(D):
    mid -= d
    if mid <= 0:
        print(i + 1, d + mid)
        break
