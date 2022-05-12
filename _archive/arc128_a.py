n = int(input())
A = list(map(int, input().split()))

dpGold = [1] + [0] * n
dpSilver = [0] + [0] * n

print(dpGold, dpSilver)
