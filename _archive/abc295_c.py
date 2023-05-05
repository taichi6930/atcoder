from collections import Counter
n = int(input())
print(sum(list(map(lambda x: x // 2, list(Counter(list(map(int, input().split()))).values())))))
