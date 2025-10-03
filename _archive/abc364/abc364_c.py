from bisect import bisect_left
from itertools import accumulate

n, x, y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# sorted_Aの累積和
cum_A = list(accumulate([0] + sorted(A, reverse=True)))
# sorted_Bの累積和
cum_B = list(accumulate([0] + sorted(B, reverse=True)))

print(min(bisect_left(cum_A, x + 1), bisect_left(cum_B, y + 1), n))
