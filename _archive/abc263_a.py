from collections import Counter
num = list(map(int, input().split()))
c = Counter(num)
print('YNeos'[not(c.most_common()[0][1] ==
      3 and c.most_common()[1][1] == 2)::2])
