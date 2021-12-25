import collections


def main():
    n, m = map(int, input().split())
    K = [None for _ in range(n)]
    A = [None for _ in range(n)]
    ANS = [0 for _ in range(n)]
    for i in range(n):
        Z = list(map(int, input().split()))
        K[i] = Z[0]
        A[i] = Z[1:]

    p, q = map(int, input().split())
    B = list(map(int, input().split()))
    for j in range(p):
        for k in range(n):
            if A[k].count(B[j]) > 0:
                ANS[k] = min(ANS[k] + 1, q)
    print(collections.Counter(ANS)[q])


if __name__ == '__main__':
    main()
