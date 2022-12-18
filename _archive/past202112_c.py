n = int(input())
dic = {i: 10000 for i in list('ABCDEF')}

for i in range(n):
    p, v = map(str, input().split())
    if v == 'AC':
        dic[p] = min(dic[p], i + 1)

for i in list('ABCDEF'):
    print(dic[i])
