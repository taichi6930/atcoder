n = int(input())
a = sorted(list(set(map(int, input().split()))))

while len(a) > 1:
    for i in range(1, len(a)):
        a[i] %= a[0]
    a = sorted(set(a))

    if a[0] == 0:
        a = a[1::]

print(*a)
