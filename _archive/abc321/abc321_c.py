k = int(input())
ansKeta = 0
import math

# kの桁数 -1 まで繰り返す
for i in range(10):
    _ansKeta = math.prod([10 - j for j in range(i + 1)])
    if ansKeta + _ansKeta >= k:
        break
