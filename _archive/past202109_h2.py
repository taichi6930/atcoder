import numpy as np


def main():
    n, x = map(int, input().split())
    dist = np.full((n, n), x + 1)
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        dist[a-1, b-1] = c
        dist[b-1, a-1] = c

    for i in range(n):
        dist[i, i] = 0

    ans = 0
    for k in range(n):
        dist = np.minimum(dist, dist[:, k, None] + dist[k])
        ans += dist[dist < x + 1].sum()

    for a in range(n - 1):
        for b in range(a + 1, n):
            if dist[a][b] == x:
                print('Yes')
                return
    print('No')


if __name__ == '__main__':
    main()
