n = int(input())
AB = [[] for _ in range(n)]
ABNum = [0 for _ in range(n)]
ABList = [0 for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    AB[a - 1].append(b)
    ABNum[a - 1] += 1
    AB[b - 1].append(a)
    ABNum[b - 1] += 1
    
