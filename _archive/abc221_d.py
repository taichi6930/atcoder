import collections


def main():
    n = int(input())
    c1 = collections.Counter()
    c1[0] = 0
    ans = collections.Counter()
    for _ in range(n):
        a, b = map(int, input().split())
        c1[a] = c1[a] + 1
        c1[a + b] = c1[a + b] - 1

    keys = sorted(list(c1.keys()) + [max(c1.keys()) + 1])
    cnt = 0
    z = 0
    for key in keys:
        cnt += c1[key]
        ans[cnt] = ans[cnt] + (key - z)
        z = key

    r = collections.deque()

    for i in range(n):
        r.append(ans[i + 1])

    print(' '.join(list(map(lambda x: str(x), r))))


if __name__ == '__main__':
    main()
