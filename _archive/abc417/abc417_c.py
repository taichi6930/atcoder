n = int(input())
A = list(map(int, input().split()))

left = [A[i] + (i + 1) for i in range(n)]
right = [-A[i] + (i + 1) for i in range(n)]

from collections import Counter

left_count = Counter(left)
right_count = Counter(right)

print(sum([left_count[k] * right_count[k] for k in left_count.keys()]))
