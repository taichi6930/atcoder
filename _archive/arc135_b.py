import math


def main():
    n = int(input())
    S = list(map(int, input().split()))
    ca = math.ceil((n + 2) / 3)

    A = [[0] * (ca), [0] * (ca), [0] * (ca)]

    for i in range(n - 1):
        A[i % 3][i // 3 + 1] = A[i % 3][i // 3] + S[i + 1] - S[i]

    A0min, A1min, A2min = min(A[0]), min(A[1]), min(A[2])

    for i in range(ca):
        if A0min < 0:
            A[0][i] -= A0min
        if A1min < 0:
            A[1][i] -= A1min
        if A2min < 0:
            A[2][i] -= A2min

    if (n + 2) % 2 == 0:
        if A[1][-1] + A[2][-1] > 0:
            print('No')
            return
    if (n + 1) % 2 == 0:
        if A[2][-1] > 0:
            print('No')
            return

    ans = [None] * (n + 2)

    fusoku = S[0] - A[0][0] - A[1][0] - A[2][0]
    for j in range(n + 2):
        if j % 3 == 2:
            ans[j] = str(A[j % 3][j // 3] + fusoku)
            continue
        ans[j] = str(A[j % 3][j // 3])
    print('Yes')
    print(' '.join(ans))


if __name__ == '__main__':
    main()
