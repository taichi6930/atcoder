from collections import Counter
n = int(input())
cS = Counter([input() for _ in range(n)])
print('Yes' if cS['For'] > cS['Against'] else 'No')
