from itertools import accumulate
n = int(input())
A = list(map(int, input().split()))
AA = [0] + list(accumulate(A))

print(AA)
