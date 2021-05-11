n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
sumA = 0
num = n - 1
for i in range(n):
    sumA += A[i] * num
    num -= 2
print(sumA)
