from collections import *
n = int(input())
A = list(map(int, input().split()))
k = len(list(Counter(A).keys()))
print(k - (1 - k % 2))
