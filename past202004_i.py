import time


def main():
    n = int(input())
    A = list(map(int, input().split()))

    for a in range(2 ** n):
        A[a] = [a, A[a]]

    B = [n for _ in range(2 ** n)]

    for i in range(n):
        l = 2 ** (n - i - 1)
        C = []
        for j in range(l):
            s = 2 * j
            g = 2 * j + 1
            if A[s][1] > A[g][1]:
                B[A[g][0]] = i
                C.append(A[s])
            else:
                B[A[s][0]] = i
                C.append(A[g])
        A = C

    for b in B:
        print(min(b + 1, n))


if __name__ == '__main__':
    main()
