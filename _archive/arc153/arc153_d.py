def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


n = int(input())
A = list(map(int, input().split()))

ans = sum([sum(str2intWithArray(list(str(i)))) for i in A])
K = set()
for _, a in enumerate(A):
    str_a = str(a)
    len_a = len(str_a)
    for i in range(1, len_a + 1):
        k = 10 ** i - a % (10 ** i)
        K.add(k)

for k in K:
    ans_a = 0
    for b in A:
        l = list(str(k + b))
        ans_a += sum(str2intWithArray(l))
    ans = min(ans, ans_a)
print(ans)
