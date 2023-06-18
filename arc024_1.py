from collections import Counter

l, r = map(int, input().split())
c1 = Counter(list(map(int, input().split())))
c2 = Counter(list(map(int, input().split())))

print(sum([min(c1[key], c2[key]) for key in list(c1.keys())]))
