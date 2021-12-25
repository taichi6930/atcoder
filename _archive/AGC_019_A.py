q, h, s, d = map(int, input().split())
n = int(input())

print((n // 2) * min(q * 8, h * 4, s * 2, d) + (n - n // 2 * 2) *
      min(q * 4, h * 2, s))
