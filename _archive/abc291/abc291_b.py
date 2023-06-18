n = int(input())
print(sum(sorted(list(map(int, input().split())))[n: -n]) / (3 * n))
