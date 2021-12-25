# 動的計画法：ナップザック DP
# No.37
# 問題: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja

def main():
    n, m = map(int, input().split())
    C = list(map(int, input().split()))

    dp = [i for i in range(n + 1)]

    for c in C:
        for i in range(c, n + 1):
            dp[i] = min(dp[i - c] + 1, dp[i])
    print(dp[n])


if __name__ == '__main__':
    main()
