import math


def main():
    n = int(input())
    A = list(map(int, input().split()))
    Bfrom0toX = [A[0]] + [None for _ in range(n - 1)]
    BfromYtoN = [None for _ in range(n - 1)] + [A[n - 1]]

    for i in range(1, n):
        Bfrom0toX[i] = math.gcd(A[i], Bfrom0toX[i - 1])
        BfromYtoN[n - 1 - i] = math.gcd(BfromYtoN[n - i], A[n - i])

    ans = 1

    Bfrom0toX = [0] + Bfrom0toX
    BfromYtoN = BfromYtoN + [0]

    for j in range(n):
        if Bfrom0toX[j] * BfromYtoN[j] == 0:
            ans = max(Bfrom0toX[j] + BfromYtoN[j], ans)
            continue
        ans = max(math.gcd(Bfrom0toX[j], BfromYtoN[j]), ans)
    print(ans)


if __name__ == '__main__':
    main()
