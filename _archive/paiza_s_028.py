from itertools import accumulate
n = int(input())
s = list(map(lambda x: int(x), list(input())))
s_sum = sum(s)

acc_s = [0] + list(accumulate(s * 2))
ans = 10 ** 10
cnt = 0
st1_num = 0
st2_num = 0

for st in range(n + 1):
    for st1 in range(max(st1_num - 1, st + 1), st + n + 1):
        swi = False
        a = acc_s[st1] - acc_s[st]
        for st2 in range(max(st2_num - 1, st1 + 1), st1 + n + 1):
            cnt += 1
            b = acc_s[st2] - acc_s[st1]
            c = acc_s[st + n] - acc_s[st2]
            ans = min(ans, max(abs(a - b), abs(a - c), abs(a - c)))
            if max(a, b, c) == a:
                swi = True
                st1_num = st1
                st2_num = st2
                break
            if min(a, b, c) == c:
                st1_num = st1
                st2_num = st2
                break
        if swi:
            break
print(ans)
