n = int(input())
A = list(map(int, input().split()))
from collections import Counter, defaultdict
cA = Counter(A)
listA = sorted(list(set(A)), reverse=True)
dA = defaultdict(int)
dA[listA[0]] = 0
for i in range(1, len(listA)):
    dA[listA[i]] = dA[listA[i - 1]] + cA[listA[i - 1]] * listA[i - 1]

# Aをfor文で回し、dA[A[i]]を出力する
# 出力する際には、1 3 4」のようにスペース区切りで出力する
print(" ".join(list(str(dA[a]) for a in A)))