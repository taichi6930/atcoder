h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
mod = 10 ** 9 + 7
dp = [[0 for _ in range(w)] for _ in range(h)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        # 今いるマスが#であるなら、パス
        if S[i][j] == '#':
            continue
        # 上に遡っていく、#であったら止める
        for a in range(h):
            # マス目がないのであればストップ
            aa = i - a - 1
            if aa < 0:
                break
            # 今いるマスが#であるなら、パス
            if S[aa][j] == '#':
                break
            dp[i][j] = (dp[i][j] + dp[aa][j]) % mod
        # 左に遡っていく、#であったら止める
        for b in range(w):
            # マス目がないのであればストップ
            bb = j - b - 1
            if bb < 0:
                break
            # 今いるマスが#であるなら、パス
            if S[i][bb] == '#':
                break
            dp[i][j] = (dp[i][j] + dp[i][bb]) % mod
        # 斜めに遡っていく、#であったら止める
        for c in range(max(i, j)):
            # マス目がないのであればストップ
            if i - c - 1 < 0 or j - c - 1 < 0:
                break
            # 今いるマスが#であるなら、パス
            if S[i - c - 1][j - c - 1] == '#':
                break
            dp[i][j] = (dp[i][j] + dp[i - c - 1][j - c - 1]) % mod

print(dp[-1][-1])
