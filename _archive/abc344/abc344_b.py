A = list()

for i in range(10**10):
    l = int(input())
    A.append(l)
    if l == 0:
        break

for a in A[::-1]:
    print(a)
