import datetime
import collections
import math
from collections import Counter, deque
from itertools import accumulate  # 累積和を求めるときに使う
from itertools import permutations  # 順列全探索で使う
from bisect import bisect_left
from pprint import pprint
from functools import lru_cache  # 同じものは再計算しない

mod = 998244353
n, m = map(int, input().split())
ans = n
for i in range(1, m - 1):
    ans = (ans * (m - 1)) % mod
ans = (ans * (m - 2)) % mod
print(ans)
