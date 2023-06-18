from collections import Counter, defaultdict
n, m = map(int, input().split())
counter = Counter()
dic = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    counter[u] += 1
    counter[v] += 1
    dic[u].append(v)
    dic[v].append(u)

s = 0

cnt = Counter()
for value in counter.values():
    cnt[value] += 1
    if value == 1:
        s = value

if cnt[1] != 2:
    exit(print('No'))
if max(cnt.keys()) > 2:
    exit(print('No'))

for i in range(n - 1):
    new_s_list = dic[s]
    if len(new_s_list) != 1:
        exit(print('No'))
    new_s = new_s_list[0]
    dic[s].remove(new_s)
    dic[new_s].remove(s)
    s = new_s

for k, v in dic.items():
    if len(v) != 0:
        exit(print('No'))
print('Yes')
