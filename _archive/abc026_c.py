from collections import *
n = int(input())
bList = defaultdict(list)
salaryList = [1 for _ in range(n)]

for i in range(2, n + 1):
    b = int(input())
    bList[b - 1].append(i - 1)


def f(num):
    if len(bList[num]) == 0:
        salaryList[num] = 1
        return

    minSalary, maxSalary = 10 ** 9, 0
    for nu in bList[num]:
        f(nu)

    for nu in bList[num]:
        minSalary = min(minSalary, salaryList[nu])
        maxSalary = max(maxSalary, salaryList[nu])
    salaryList[num] = minSalary + maxSalary + 1


f(0)
print(salaryList[0])
