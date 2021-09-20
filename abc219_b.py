def str2intWithArray(Array):  # 文字の配列を数字の配列に変換する
    return list(map(lambda x: int(x), Array))


def main():
    S = [input() for _ in range(3)]
    T = str2intWithArray(list(input()))
    ANS = ''

    for t in T:
        ANS += S[t - 1]
    print(ANS)


if __name__ == '__main__':
    main()
