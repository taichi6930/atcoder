from itertools import permutations  # 順列全探索で使う


def main():
    n = int(input())
    s = input()
    P = list(permutations([list(s)[i - 1] for i in range(1, n + 1)]))
    for p in P:
        t = ''.join(p)
        if s == t or s == t[::-1]:
            continue
        print(t)
        return

    print('None')


if __name__ == '__main__':
    main()
