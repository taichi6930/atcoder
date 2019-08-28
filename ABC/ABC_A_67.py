a, b = map(int, input().split())
sign = a % 3 == 0 or b % 3 == 0 or (a+b) % 3 == 0
print("Possible" if sign else "Impossible")
