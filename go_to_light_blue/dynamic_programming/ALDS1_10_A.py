from collections import deque


def main():
    n = int(input())
    dp = deque([1, 1])
    for i in range(2, n + 1):
        a = dp[i - 1] + dp[i - 2]
        dp.append(a)
    print(dp[n])


if __name__ == '__main__':
    main()
