from time import time

start = time()

n = int(input())
sList = []
for i in range(n):
    sList.append(input())

print(str(time() - start) + "s")
