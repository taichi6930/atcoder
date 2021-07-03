n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
j = [abs(t - j * 0.006 - a) for j in h]
print(h.index(min(h)) + 1)
