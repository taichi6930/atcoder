def str2intWithArray(Array):  # 文字の配列を数字の配列に変換する
    return list(map(lambda x: int(x), Array))


def main():
    s = input()
    d = s[-1]
    s = s[0: -1]

    # 左の 14 桁のうち、左から奇数番目の数 (一番左の数を 1 番目と数えます) をすべて足し、その値を 3 倍します。
    a = (3 * sum(str2intWithArray(s[0::2])) +
         sum(str2intWithArray(s[1::2]))) % 10
    print('Yes' if int(d) == int(a) else 'No')


if __name__ == '__main__':
    main()
