p, q = map(str, input().split())
lis = [0, 3, 4, 8, 9, 14, 23]
print(abs(lis[ord(p) - 65] - lis[ord(q) - 65]))
