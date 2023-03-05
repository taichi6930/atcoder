from collections import defaultdict
n = int(input())
dic = defaultdict(defaultdict(list))
for i in range(n):
    x, y, z = input().split()
    dic[int(y)].append(('0' + z)[-2:] + '_' + x)

ans = []

for key in sorted(dic.keys(), reverse=True):
    for i in sorted(dic[key], reverse=True):
        ans.append(i.split('_')[-1])

for a in ans[::-1]:
    print(a)
