s = input()
n = int(input())
sSet = sorted(list(set(list(s))))
sSum = 0
for a in range(len(sSet)):
    engList = [i for i, x in enumerate(s) if x == sSet[a]]
    print(len(s) * len(engList)-sum(engList))
