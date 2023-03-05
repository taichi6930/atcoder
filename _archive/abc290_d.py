T = int(input())
a = 0

for t in range(T):
    n, d, k = map(int, input().split())
    x = (a + d) % n
