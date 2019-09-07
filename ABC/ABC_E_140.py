import time

n = int(input())
start = time.time()
# p = list(map(int, input().split()))
p = [1, 2, 3, 4, 5]
sump = 0
for i in range(n-1):
    for j in range(i+2, n+1):
        # sump += sorted(p[i:j])[-2]
        sump += sorted(p[0:3])[-2]
print(sump)

print(time.time() - start)
