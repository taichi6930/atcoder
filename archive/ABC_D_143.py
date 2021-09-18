import bisect


def main():
    cnt = 0
    n = int(input())
    L = sorted(list(map(int,  input().split())))
    for a in range(0, n - 2):
        for b in range(a + 1, n - 1):
            k = L[a] + L[b]
            index = bisect.bisect_left(L, k)
            cnt += index - b - 1
    print(cnt)


if __name__ == '__main__':
    main()
