from itertools import permutations  # 順列全探索で使う


def main():
    permutation = list(permutations([i for i in range(3)]))
    nml = list(map(int, input().split()))
    pqr = list(map(int, input().split()))
    ans = 0
    for per in permutation:
        k = 1
        for j in range(3):
            k *= nml[j] // pqr[per[j]]
        ans = max(k, ans)

    print(ans)


if __name__ == '__main__':
    main()
