from copy import deepcopy
h, w, a, b = map(int, input().split())
dp = [True] * (h * w)

ans = 0


def depth(dp, num, aa, bb):
    global ans

    # aを全て使い切ったら終了
    if aa == 0:
        ans += 1
        return

    if aa < 0 or bb < 0:
        return

    # aを使いきれない場合終了
    if h * w - num < aa * 2:
        return

    # 既に使われている場所であれば次に行く
    if not(dp[num]):
        depth(dp, num + 1, aa, bb)
        return

    # 縦に2つマスを使うとき
    if num + w < h * w:
        newDp = deepcopy(dp)
        newDp[num] = False
        newDp[num + w] = False
        depth(newDp, num + 1, aa - 1, bb)

    # 横に2つマスを使うとき
    if (num + 1) % w != 0:
        newDp = deepcopy(dp)
        newDp[num] = False
        newDp[num + 1] = False
        depth(newDp, num + 1, aa - 1, bb)

    newDp = deepcopy(dp)
    newDp[num] = False
    depth(newDp, num + 1, aa, bb - 1)


aa = 0 + a
bb = 0 + b
newDp = deepcopy(dp)
depth(newDp, 0, aa, bb)

print(ans)
