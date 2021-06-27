n = int(input())
a = sorted(list(map(int, input().split())))

for i in range(n):
    if a[i] != i + 1:
        print("No")
        exit()

print("Yes")
