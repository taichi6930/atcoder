import re
lis = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]
ansLis = ['0'] * 7

inp = list(input())
for i, num in enumerate(inp):
    if num == '0':
        continue
    if i == 0:
        exit(print('No'))
    ansLis[lis[i]] = '1'

ansLis = ''.join(ansLis)

for _ in range(7):
    ansLis = ansLis.replace('00', '0')

print('Yes' if ansLis.find('101') >= 0 else 'No')
