x = list(map(int, input().split()))
a = x[0] - x[4]
b = x[1] - x[5]
c = x[2] - x[4]
d = x[3] - x[5]

print(abs(a * d - b * c) / 2)
