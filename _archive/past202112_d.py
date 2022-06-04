from pprint import *
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Y = [[i + 1, A[i] + B[i], A[i]] for i in range(n)]
Y.sort(key=lambda x: x[2], reverse=True)
Y.sort(key=lambda x: x[1], reverse=True)
print(' '.join([str(Y[i][0]) for i in range(n)]))
