def cnt_step(Arr, x):
    ans = 0

    n = len(Arr)

    for i in range(n):
        minus = max(0, Arr[i] - x)

        if minus == 0:
            continue

        ans += minus
        Arr[i] -= minus
        if i + 1 != n:
            Arr[i + 1] -= minus
    return ans


def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    B = [A[i] + A[i + 1] for i in range(n - 1)]
    C = [B[n - 2 - j] for j in range(n - 1)]

    print(min(int(cnt_step(B, x)), int(cnt_step(C, x))))


if __name__ == '__main__':
    main()
