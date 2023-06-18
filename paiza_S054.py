from collections import defaultdict
n, x = map(int, input().split())
VWC = sorted([list(map(int, input().split()))
             for _ in range(n)], key=lambda x: x[0], reverse=True)

ans = -1
k = 0
dicK = defaultdict()


def f(v_old_sum, w_old_sum, cnt):
    global ans, x, k
    k += 1
    if v_old_sum == x:
        if ans is None:
            ans = w_old_sum
            return
        ans = max(ans, w_old_sum)
        return
    if cnt >= n:
        return
    v, w, c = VWC[cnt]
    for i in range(c + 1):
        v_sum = v_old_sum + v * i
        if v_sum > x:
            return
        w_sum = w_old_sum + w * i
        f(v_sum, w_sum, cnt + 1)


f(0, 0, 0)
print(ans)
