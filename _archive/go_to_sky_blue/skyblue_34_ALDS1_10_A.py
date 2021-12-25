# 動的計画法：ナップザック DP
# No.34
# 問題: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja

def main():
    n = int(input())
    dp = [1, 1] + [None] * 43

    for i in range(2, 45):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])


if __name__ == '__main__':
    main()
