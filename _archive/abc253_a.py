a, b, c = map(int, input().split())
abcList = sorted([a, b, c])

print('Yes' if b == abcList[1] else 'No')
