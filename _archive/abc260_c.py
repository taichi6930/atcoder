n, x, y = map(int, input().split())

R = 1
B = 0

for i in range(n - 1):
    B += x * R
    R += B
    B *= y

print(B)
