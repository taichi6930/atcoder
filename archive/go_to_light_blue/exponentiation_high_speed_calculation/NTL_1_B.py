import collections
import math

mod = 10 ** 9 + 7


def main():
    m, n = map(int, input().split())
    A = collections.deque([m])

    for i in range(1, n):
        a = A[-1]
        A.append((a ** 2) % mod)
        if A[-1] == 1:
            break
        if 2 ** i > n:
            break

    ans = 1
    k = n

    for j in range(n):
        w = int(math.log(k, 2))
        ans = (ans * A[min(w, len(A) - 1)]) % mod
        k -= 2 ** w
        if k <= 0:
            break

    print(ans)


if __name__ == '__main__':
    main()
