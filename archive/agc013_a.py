import collections
import math

alphaList = list("abcdefghijklmnopqrstuvwxyz")


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0]

    for i in range(n - 1):
        B.append(A[i + 1] - A[i])

    ans = 1
    swi = 0

    for j in range(n):
        # 0であれば続行する
        if B[j] == 0:
            continue

        if B[j] * swi >= 0:
            swi = B[j] // abs(B[j])
            continue
        else:
            swi = 0
            ans += 1
            continue

    print(ans)


if __name__ == '__main__':
    main()
