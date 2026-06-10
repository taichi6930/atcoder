n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i, a in enumerate(A):
    if i + 1 != B[a - 1]:
        print("No")
        exit()
print("Yes")
