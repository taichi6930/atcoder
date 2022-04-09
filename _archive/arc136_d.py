import collections
n = int(input())
A = sorted(list(map(str, input().split())))

B1 = [[], [], [], [], [], []]
B2 = [[], [], [], [], [], []]

for i in range(n):
    lenQ = len(A[i])
    for j in range(lenQ - 1):
        B2[j].append(A[i][lenQ - j - 1:lenQ])
    B1[lenQ - 1].append(A[i][:lenQ])

for i in range(len(A[-1])):
    cB1 = collections.Counter(B1[i])
    cB2 = collections.Counter(B2[i])
    for j in range()

print(B1)
print(B2)
