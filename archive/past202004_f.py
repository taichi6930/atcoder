import collections


def main():
    n = int(input())
    B = [collections.deque() for _ in range(n)]

    Blis = []

    ans = 0

    for i in range(n):
        a, b = map(int, input().split())

        B[a - 1].append(b)
    for j in range(n):
        Blis += B[j]
        if len(Blis) == 0:
            print(ans)
            continue
        ans += max(Blis)
        Blis.remove(max(Blis))
        print(ans)


if __name__ == '__main__':
    main()
