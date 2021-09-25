from collections import deque


def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    if n == 2:
        print(1)
        return
    sumA = sum(A[1:-1])
    p = sumA // (n - 2)
    q = sumA % (n - 2)

    B = deque([0] + [p] * (n - 2 - q) + [p + 1] * q + [0])

    for i in range(len(B) - 1):
        ans += (1 + (B[i + 1] - B[i]) ** 2) ** 0.5
    print(ans)


if __name__ == '__main__':
    main()
