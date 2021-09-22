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
        Blis += list(B[j])
        Blis.sort()
        if len(Blis) == 0:
            print(ans)
            continue
        ans += Blis[-1]
        Blis.pop()
        print(ans)


if __name__ == '__main__':
    main()
