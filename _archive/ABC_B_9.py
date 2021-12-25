N = int(input())
a = [int(input()) for i in range(N)]
print(sorted(list(set(a)), reverse=True)[1])
