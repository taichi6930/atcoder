from collections import deque


def main():
    n = int(input())
    A = [[0 for _ in range(i + 1)] +
         list(map(int, input().split())) for i in range(n - 1)]
    ans = None
    for i in range(3 ** (n + 1)):
        k = 0
        a0, a1, a2 = deque(), deque(), deque()
        q = i * 1
        if q % 3 != 0:
            continue
        for j in range(1, n + 1):

            if q % 3 == 0:
                a0.append(j)
            elif q % 3 == 1:
                a1.append(j)
                q -= 1
            elif q % 3 == 2:
                a2.append(j)
                q -= 2
            q = q // 3

        lena0, lena1, lena2 = len(a0), len(a1), len(a2)

        if lena0 > 1:
            for a0s in range(lena0 - 1):
                for a0f in range(a0s + 1, lena0):
                    k += A[a0[a0s] - 1][a0[a0f] - 1]

        if lena1 > 1:
            for a1s in range(lena1 - 1):
                for a1f in range(a1s + 1, lena1):
                    k += A[a1[a1s] - 1][a1[a1f] - 1]

        if lena2 > 1:
            for a2s in range(lena2 - 1):
                for a2f in range(a2s + 1, lena2):
                    k += A[a2[a2s] - 1][a2[a2f] - 1]
        if ans is None:
            ans = k
        ans = max(ans, k)
    print(ans)


if __name__ == '__main__':
    main()
