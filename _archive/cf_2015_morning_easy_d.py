def main():
    n = int(input())
    S = list(input())

    C = collections.Counter(S)

    for i in range(n):
        if C[S[n - i - 1]] == 1:
            S.pop(n - i - 1)


if __name__ == '__main__':
    main()

import collections