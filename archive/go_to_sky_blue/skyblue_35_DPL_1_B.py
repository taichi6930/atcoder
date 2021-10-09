# 動的計画法：ナップザック DP
# No.35
# 問題: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja

def main():
    N, W = map(int, input().split())

    # dp[i][w]: i番目までの品物の中から重さがwを超えないように選んだ時の、価値の総和の最大値
    dp = [[None] * (W + 1) for _ in range(N + 1)]

    # 選んでいないとき dp[0][w] = 0となる（初期条件）
    for w in range(W + 1):
        dp[0][w] = 0

    for i in range(N):
        value, weight = map(int, input().split())
        for w in range(W + 1):
            # wがweight以上の時は、2択になる
            # weight分重くなった分、valueを得る
            if w >= weight:
                dp[i + 1][w] = max(dp[i][w - weight] + value, dp[i][w])
                continue

            # wがweightを超えなければ、新しい荷物は入れられないため、
            # そのまま引き継ぐ
            dp[i + 1][w] = dp[i][w]

    # dp[N][W]: N番目までの品物の中から重さがWを超えないように選んだ時の、価値の総和の最大値
    print(dp[N][W])


if __name__ == '__main__':
    main()
