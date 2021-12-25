from bisect import bisect_right


def main():
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    ans = [None] * q
    for i in range(q):
        x = int(input())
        ans[i] = len(a) - bisect_right(a, x - 1)

    for j in range(q):
        print(ans[j])


if __name__ == '__main__':
    main()
