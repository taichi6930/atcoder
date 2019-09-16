[(a, b, c), (d, e, f), (g, h, i)] = [
    map(int, input().split()) for i in range(3)]

q1 = a - b == d - e == g - h
q2 = a - c == d - f == g - i
q3 = a - d == b - e == c - f
q4 = a - g == b - h == c - i

print("Yes" if q1 and q2 and q3 and q4 else "No")
