N, M = map(int, input().split())
A = []
B = []

a, b = map(int, input().split())

A.append(a)
B.append(b)

if N != 1:
    for n in range(N-1):
        a, b = map(int, input().split())
        swi = 0
        BSum = 0
        for j in range(len(A)):
            if BSum > M:
                swi = 1
                break
            else:
                if A[j] > a:
                    A.insert(j, a)
                    B.insert(j, b)
                    swi = 1
                    break
                elif A[j] == a:
                    B[j] += b
                    swi = 1
                    break
            BSum += b
        if swi == 0:
            A.append(a)
            B.append(b)

cntSum = 0
moneySum = 0

print(A, B)

for n in range(N):
    if cntSum + B[n] > M:
        moneySum += A[n] * (M - cntSum)
        cntSum += M - cntSum
        break
    else:
        cntSum += B[n]
        moneySum += A[n] * B[n]

print(moneySum)
