n = int(input())
print(sum(sorted(list(map(int, input().split())), reverse=True)[1:n * 2:2]))
