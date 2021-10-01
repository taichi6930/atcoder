# 動的計画法：ナップザック DP
# No.36
# 問題: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja

def main():
    N, W = map(int, input().split())

    # dp[w]: 重さがwを超えないように選んだ時の、価値の総和の最大値
    # 今回は複数使用可能
    # 選んでいないとき dp[w] = 0となる（初期条件）
    dp = [0] * (W + 1)

    for i in range(N):
        v, w = map(int, input().split())
        for j in range(w, W + 1):
            # wがweight以上の時に絞って考えているので、2択になる
            dp[j] = max(dp[j - w] + v, dp[j])

    # dp[W]: 重さがWを超えないように選んだ時の、価値の総和の最大値
    print(max(dp))


if __name__ == '__main__':
    main()
