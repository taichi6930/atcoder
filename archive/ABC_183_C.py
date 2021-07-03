import itertools


def main():
    n, k = map(int, input().split())
    t = [None] * n

    for i in range(n):
        t[i] = list(map(int, input().split()))

    nums = list(range(1, n))
    ans = 0

    for i in itertools.permutations(nums):
        i = [0]+list(i)
        sums = 0

        for j in range(n):
            sums += t[i[j]][i[(j+1) % n]]
        if sums == k:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
