import collections


def main():
    n = int(input())
    A = list(map(int,  input().split()))
    ans = 0
    c = collections.Counter()

    for i in range(n):
        ans += c[i + 1 - A[i]]
        c[i + 1 + A[i]] += 1
        print(c)

    print(ans)


if __name__ == '__main__':
    main()
