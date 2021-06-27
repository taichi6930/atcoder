n = int(input())
l = list(map(int, input().split()))
ans = 0

if n > 3:
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                a, b, c = l[i], l[j], l[k]
                if (a != b and b != c and c != a) and max(a, b, c) < (a + b + c) - max(a, b, c):
                    ans += 1

print(ans)
