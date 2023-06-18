import collections


def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    C = collections.Counter(A)
    # 1種類であれば答えはA[0]
    if len(C.keys()) == 1:
        print(A[0])
        return

    no1value = C.most_common()[0][1]
    no2value = C.most_common()[1][1]

    # no1の数が過半数超えていなかったら?になる
    if no1value <= n / 2 or no2value >= n / 2:
        print("?")
        return

    print(C.most_common()[0][0])


if __name__ == '__main__':
    main()
