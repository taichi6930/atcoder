n = int(input())
a1, a2 = [list(map(int, input().split())) for i in range(2)]
print(max(sum(a1[0:i+1]) + sum(a2[i:n]) for i in range(n)))
