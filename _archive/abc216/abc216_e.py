import collections


def main():
    n, k = map(int, input().split())
    A = collections.deque(
        sorted(list(map(int, input().split())) + [0], reverse=True))
    ans = 0

    for i in range(n):
        keyNum = (- A[i + 1] + A[i]) * (i + 1)
        if keyNum > k:

            ans += (k // (i + 1)) * \
                (A[i] + (A[i] - (k // (i + 1)) + 1)) // 2 * (i + 1)
            k -= (k // (i + 1)) * (i + 1)
            ans += ((A[i] - (k // (i + 1)) + 1) - 1) * k
            break
        ans += ((A[i] - A[i + 1]) * ((A[i + 1] + 1) + A[i]) // 2) * (i + 1)
        k -= keyNum
    print(ans)


if __name__ == '__main__':
    main()
