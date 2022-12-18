n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
A1 = []
A2 = []
for a in A:
    if a % 2 == 0:
        A2.append(a)
        continue
    A1.append(a)
ansList = [-1]
A1 = sorted(A1, reverse=True)
A2 = sorted(A2, reverse=True)

if len(A1) >= 2:
    ansList.append(A1[0] + A1[1])
if len(A2) >= 2:
    ansList.append(A2[0] + A2[1])
print(max(ansList))
