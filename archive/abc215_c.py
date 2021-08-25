from itertools import permutations  # 順列全探索で使う


def main():
    A = set()

    s, k = map(str, input().split())
    s = sorted(list(s))
    P = list(permutations([i for i in range(len(s))]))
    for p in P:
        string = ''
        for i in range(len(s)):
            string += s[p[i]]
        A.add(string)
    print(sorted(list(A))[int(k) - 1])


if __name__ == '__main__':
    main()
