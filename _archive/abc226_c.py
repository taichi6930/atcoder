import collections


def main():
    n = int(input())
    T = collections.deque()
    A = collections.deque()

    for i in range(n):
        Z = list(map(int, input().split()))
        T.append(Z[0])
        a = []
        if Z[1] != 0:
            a = Z[2:]
        A.append(a)

    C = A[-1]
    B = set([n])

    for i in range(10 ** 9):
        D = [] + C
        if len(C) == 0:
            break
        C = []
        B = set(B) | set(D)
        for d in D:
            C += A[d - 1]
    B = list(B)

    ans = 0
    for b in B:
        ans += T[b - 1]
    print(ans)


if __name__ == '__main__':
    main()
