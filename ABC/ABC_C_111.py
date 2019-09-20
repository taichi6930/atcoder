from collections import Counter

n = int(input())
abList = list(map(int, input().split()))
a = abList[0::2]
b = abList[1::2]
print(a, b)

tmp_list = [1, 1, 1, 1, 0, 1, 1]
A = Counter(a)

print(A.most_common()[0][0])
