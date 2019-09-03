import math

a, b = map(str, input().split())
num = int(a + b)
print("Yes" if math.floor(math.sqrt(num)) -
      math.ceil(math.sqrt(num)) == 0 else "No")
