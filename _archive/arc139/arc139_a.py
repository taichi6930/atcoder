from collections import deque
n = int(input())
T = list(map(int, input().split()))
ANS = deque([2 ** T[0]])

for i, t in enumerate(T):
    if i == 0:
        continue
    a = 2 ** t
    k = (ANS[-1] // (2 * a)) * (2 * a)
    for j in range(10 ** 9):
        if k + a + j * 2 * a > ANS[-1]:
            ANS.append(k + a + j * 2 * a)
            break

print(ANS[-1])
