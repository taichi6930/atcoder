n, m = map(int, input().split())
Theta = abs((n % 12) * 30 - m * 5.5)
print(Theta if Theta < 180 else 360 - Theta)
